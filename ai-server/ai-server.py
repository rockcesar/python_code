# -*- coding: utf-8 -*-

# Developed with the help of Gemini AI
# Prerequisites (it will downloads heavy files, Nvidia, etc.):

# USE THIS COMMAND FOR NVIDIA (DON'T USE IT IN LOW INTERNET CONNECTION)
# pip install torch transformers accelerate

# USE THIS COMMAND FOR CPU
# pip install torch --index-url https://download.pytorch.org/whl/cpu
# pip install transformers accelerate

import http.server
import json
import socket
import urllib.parse
import urllib.request
from http import HTTPStatus

# ==========================================
# IA REAL: Qwen 2.5 (0.5B Instruct) ~320 MB
# ==========================================
AI_AVAILABLE = False
tokenizer = None
model = None

try:
    from transformers import AutoModelForCausalLM, AutoTokenizer
    import torch
    
    # Modelo open-source real y conversacional de ~320 MB
    MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
    print(f"[IA] Cargando modelo neuronal real: {MODEL_NAME} (~320 MB)...")
    
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, 
        torch_dtype=torch.float32, 
        device_map="auto"
    )
    AI_AVAILABLE = True
    print("[IA] ¡Modelo cargado exitosamente en memoria!")
except Exception as e:
    print(f"[ADVERTENCIA] No se pudo cargar el modelo de IA: {e}")

def check_internet():
    """Verifica si hay conexión a internet."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=1.5)
        return True
    except OSError:
        return False

def web_search(query):
    """Busca en internet si hay conexión disponible para enriquecer el contexto."""
    if not check_internet():
        return None
    try:
        encoded_query = urllib.parse.quote(query)
        url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=3) as response:
            html = response.read().decode("utf-8")
            from html.parser import HTMLParser
            class SnippetParser(HTMLParser):
                def __init__(self):
                    super().__init__()
                    self.in_snippet = False
                    self.snippets = []
                def handle_starttag(self, tag, attrs):
                    if tag == 'a' and any(attr[0] == 'class' and 'result__snippet' in attr[1] for attr in attrs):
                        self.in_snippet = True
                def handle_endtag(self, tag):
                    if tag == 'a': self.in_snippet = False
                def handle_data(self, data):
                    if self.in_snippet: self.snippets.append(data.strip())
            parser = SnippetParser()
            parser.feed(html)
            if parser.snippets:
                return " ".join(parser.snippets[:2])
    except Exception:
        pass
    return None

def generate_ai_response(prompt):
    """Genera la respuesta inteligente utilizando el modelo Qwen 2.5 de 0.5B de forma óptima."""
    context = ""
    search_result = web_search(prompt)
    if search_result:
        context = f"Información web de referencia: {search_result}\n\n"

    full_prompt = f"{context}Usuario: {prompt}\nAsistente:"

    if AI_AVAILABLE and model and tokenizer:
        # 1. Tokenizar incluyendo la máscara de atención explícitamente
        inputs = tokenizer(full_prompt, return_tensors="pt", padding=True)
        
        # 2. Generar pasando input_ids y attention_mask para evitar el warning
        outputs = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
        
        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        if "Asistente:" in response_text:
            response_text = response_text.split("Asistente:")[-1].strip()
            
        return response_text, bool(search_result)
    else:
        return f"Modo Offline: Recibí tu consulta '{prompt}'.", False

"""
def generate_ai_response(prompt):
    #Genera la respuesta inteligente utilizando el modelo Qwen 2.5 de 0.5B.
    context = ""
    search_result = web_search(prompt)
    if search_result:
        context = f"Información web de referencia: {search_result}\n\n"

    # Estructura de chat estándar para modelos Instruct
    full_prompt = f"{context}Usuario: {prompt}\nAsistente:"

    if AI_AVAILABLE and model and tokenizer:
        inputs = tokenizer(full_prompt, return_tensors="pt")
        outputs = model.generate(
            inputs.input_ids,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extraer solo la respuesta del asistente
        if "Asistente:" in response_text:
            response_text = response_text.split("Asistente:")[-1].strip()
            
        return response_text, bool(search_result)
    else:
        return f"Modo Offline: Recibí tu consulta '{prompt}'. (Instala torch y transformers para habilitar la inferencia neuronal).", False
"""

class AIHTTPServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode("utf-8"))
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/chat":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                user_message = data.get("message", "")
                
                answer, used_web = generate_ai_response(user_message)
                
                response_payload = {
                    "response": answer,
                    "web_searched": used_web,
                    "offline": not check_internet()
                }
                
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(response_payload).encode("utf-8"))
            except Exception as e:
                self.send_response(HTTPStatus.BAD_REQUEST)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()


# Interfaz web interactiva embebida (Cero frameworks externos)
HTML_PAGE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IA Local Qwen 2.5 (0.5B) - Puerto 3000</title>
    <style>
        body { font-family: system-ui, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; display: flex; flex-direction: column; height: 100vh; }
        header { background: #1e293b; padding: 1rem; text-align: center; border-bottom: 1px solid #334155; font-size: 1.1rem; font-weight: bold; }
        #chat-container { flex: 1; overflow-y: auto; padding: 1rem; display: flex; flex-direction: column; gap: 1rem; max-width: 800px; width: 100%; margin: 0 auto; box-sizing: border-box; }
        .message { padding: 0.75rem 1rem; border-radius: 0.5rem; max-width: 80%; line-height: 1.5; word-break: break-word; }
        .user { background: #2563eb; align-self: flex-end; }
        .ai { background: #334155; align-self: flex-start; border: 1px solid #475569; }
        .meta { font-size: 0.7rem; color: #94a3b8; margin-top: 0.25rem; display: block; }
        #input-container { background: #1e293b; padding: 1rem; display: flex; gap: 0.5rem; max-width: 800px; width: 100%; margin: 0 auto; box-sizing: border-box; border-top: 1px solid #334155; }
        input { flex: 1; padding: 0.75rem; border-radius: 0.375rem; border: 1px solid #475569; background: #0f172a; color: #fff; font-size: 1rem; outline: none; }
        button { padding: 0.75rem 1.5rem; background: #16a34a; color: #fff; border: none; border-radius: 0.375rem; font-weight: bold; cursor: pointer; }
        button:hover { background: #15803d; }
    </style>
</head>
<body>
    <header>🧠 Qwen 2.5 (0.5B) - Servidor Puro Python 3 (Puerto 3000)</header>
    <div id="chat-container">
        <div class="message ai">¡Hola! Modelo de IA de ~320 MB cargado localmente. Pregúntame lo que necesites.</div>
    </div>
    <div id="input-container">
        <input type="text" id="user-input" placeholder="Escribe tu mensaje..." autofocus>
        <button onclick="sendMessage()">Enviar</button>
    </div>
    <script>
        const chatContainer = document.getElementById('chat-container');
        const userInput = document.getElementById('user-input');
        userInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') sendMessage(); });

        async function sendMessage() {
            const text = userInput.value.trim();
            if (!text) return;
            appendMessage(text, 'user');
            userInput.value = '';
            const loadingId = appendMessage('Pensando...', 'ai');

            try {
                const res = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
                const data = await res.json();
                document.getElementById(loadingId).remove();
                let metaText = data.offline ? '📴 Modo 100% Offline' : (data.web_searched ? '🌐 Enriquecido con Internet' : '💻 Inferencia Local');
                appendMessage(data.response + `<span class="meta">${metaText}</span>`, 'ai');
            } catch (err) {
                document.getElementById(loadingId).remove();
                appendMessage('Error de comunicación con el servidor.', 'ai');
            }
        }

        function appendMessage(html, sender) {
            const div = document.createElement('div');
            div.className = `message ${sender}`;
            div.innerHTML = html;
            const id = 'msg-' + Math.random().toString(36).substring(2);
            div.id = id;
            chatContainer.appendChild(div);
            chatContainer.scrollTop = chatContainer.scrollHeight;
            return id;
        }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    server_address = ('', 3000)
    httpd = http.server.HTTPServer(server_address, AIHTTPServer)
    print("==================================================")
    print("🚀 Servidor IA Qwen corriendo en http://localhost:3000")
    print("Puro Python 3 - Sin Frameworks Web")
    print("==================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[Servidor] Apagando...")
        httpd.server_close()
