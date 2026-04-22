# -*- coding: utf-8 -*-
# ==============================================================================
# LATINCHAIN CODE - LENGUAJE DE PROGRAMACIÓN EN ESPAÑOL MULTIPLATAFORMA
# Creador: Lcdo. César Cordero
# ==============================================================================
# 
# Este programa es software libre: puedes redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General de GNU (GPLv3) tal como 
# está publicada por la Free Software Foundation, ya sea la versión 3 
# de la Licencia, o (a tu elección) cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# COMERCIALIZACIÓN o ADECUACIÓN PARA UN PROPÓSITO PARTICULAR. 
# Consulta la Licencia Pública General de GNU para más detalles.
#
# Deberías haber recibido una copia de la Licencia Pública General de GNU
# junto con este programa. Si no es así, visita <https://www.gnu.org/licenses/>.
# ==============================================================================

import sys
import re
import pickle
import os

# Forzar salida de consola a UTF-8 (Previene errores en Windows al imprimir caracteres especiales)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# --- 1. ANALIZADOR LÉXICO (LEXER) ---
# Convierte el código fuente en tokens comprensibles

TOKEN_TYPES = [
    ('COMMENT', r'//.*'),
    ('KEYWORD', r'\b(variable|si|mientras|imprimir|verdadero|falso)\b'),
    ('IDENTIFIER', r'[a-zA-Z_áéíóúÁÉÍÓÚñÑüÜ][a-zA-Z0-9_áéíóúÁÉÍÓÚñÑüÜ]*'),
    ('NUMBER', r'\d+(\.\d+)?'),
    ('STRING', r'"[^"]*"'),
    ('OPERATOR', r'==|!=|<=|>=|<|>|\+|-|\*|/|='),
    ('PUNCTUATION', r'[\(\)\{\};]'),
    ('WHITESPACE', r'\s+'),
]

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        while self.pos < len(self.text):
            match = None
            for type_, regex in TOKEN_TYPES:
                pattern = re.compile(regex)
                match = pattern.match(self.text, self.pos)
                if match:
                    value = match.group(0)
                    if type_ not in ['WHITESPACE', 'COMMENT']:
                        if type_ == 'STRING':
                            value = value[1:-1] # Quitar comillas
                        elif type_ == 'NUMBER':
                            value = float(value) if '.' in value else int(value)
                        self.tokens.append(Token(type_, value))
                    self.pos = match.end(0)
                    break
            if not match:
                raise SyntaxError(f"Carácter ilegal en la posición {self.pos}: {self.text[self.pos]}")

# --- 2. ANALIZADOR SINTÁCTICO (PARSER) ---
# Crea un Árbol de Sintaxis Abstracta (AST) a partir de los tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, type_, value=None):
        tok = self.current()
        if tok and tok.type == type_ and (value is None or tok.value == value):
            self.pos += 1
            return tok
        expected = value if value else type_
        got = tok.value if tok else "EOF"
        raise SyntaxError(f"Se esperaba '{expected}', se obtuvo '{got}'")

    def parse(self):
        statements = []
        while self.current() is not None:
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        tok = self.current()
        if tok.type == 'KEYWORD':
            if tok.value == 'variable': return self.parse_var_decl()
            if tok.value == 'imprimir': return self.parse_print()
            if tok.value == 'si': return self.parse_if()
            if tok.value == 'mientras': return self.parse_while()
        
        if tok.type == 'IDENTIFIER':
            return self.parse_assignment()
            
        raise SyntaxError(f"Declaración inválida comenzando con: {tok.value}")

    def parse_var_decl(self):
        self.eat('KEYWORD', 'variable')
        var_name = self.eat('IDENTIFIER').value
        self.eat('OPERATOR', '=')
        expr = self.parse_expression()
        self.eat('PUNCTUATION', ';')
        return ('VAR_DECL', var_name, expr)

    def parse_assignment(self):
        var_name = self.eat('IDENTIFIER').value
        self.eat('OPERATOR', '=')
        expr = self.parse_expression()
        self.eat('PUNCTUATION', ';')
        return ('ASSIGN', var_name, expr)

    def parse_print(self):
        self.eat('KEYWORD', 'imprimir')
        self.eat('PUNCTUATION', '(')
        expr = self.parse_expression()
        self.eat('PUNCTUATION', ')')
        self.eat('PUNCTUATION', ';')
        return ('PRINT', expr)

    def parse_if(self):
        self.eat('KEYWORD', 'si')
        self.eat('PUNCTUATION', '(')
        cond = self.parse_expression()
        self.eat('PUNCTUATION', ')')
        self.eat('PUNCTUATION', '{')
        body = []
        while self.current() and not (self.current().type == 'PUNCTUATION' and self.current().value == '}'):
            body.append(self.parse_statement())
        self.eat('PUNCTUATION', '}')
        return ('IF', cond, body)

    def parse_while(self):
        self.eat('KEYWORD', 'mientras')
        self.eat('PUNCTUATION', '(')
        cond = self.parse_expression()
        self.eat('PUNCTUATION', ')')
        self.eat('PUNCTUATION', '{')
        body = []
        while self.current() and not (self.current().type == 'PUNCTUATION' and self.current().value == '}'):
            body.append(self.parse_statement())
        self.eat('PUNCTUATION', '}')
        return ('WHILE', cond, body)

    def parse_expression(self):
        return self.parse_comparison()

    def parse_comparison(self):
        node = self.parse_term()
        while self.current() and self.current().type == 'OPERATOR' and self.current().value in ('==', '!=', '<', '>', '<=', '>='):
            op = self.eat('OPERATOR').value
            right = self.parse_term()
            node = ('BIN_OP', op, node, right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current() and self.current().type == 'OPERATOR' and self.current().value in ('+', '-'):
            op = self.eat('OPERATOR').value
            right = self.parse_factor()
            node = ('BIN_OP', op, node, right)
        return node

    def parse_factor(self):
        node = self.parse_primary()
        while self.current() and self.current().type == 'OPERATOR' and self.current().value in ('*', '/'):
            op = self.eat('OPERATOR').value
            right = self.parse_primary()
            node = ('BIN_OP', op, node, right)
        return node

    def parse_primary(self):
        tok = self.current()
        if tok.type == 'NUMBER':
            self.eat('NUMBER')
            return ('NUM', tok.value)
        elif tok.type == 'STRING':
            self.eat('STRING')
            return ('STR', tok.value)
        elif tok.type == 'IDENTIFIER':
            self.eat('IDENTIFIER')
            return ('VAR', tok.value)
        elif tok.type == 'KEYWORD' and tok.value in ('verdadero', 'falso'):
            self.eat('KEYWORD')
            return ('BOOL', True if tok.value == 'verdadero' else False)
        raise SyntaxError(f"Expresión inesperada: {tok.value}")

# --- 3. COMPILADOR (AST a Bytecode) ---
# Convierte el AST en instrucciones de Máquina Virtual

class Compiler:
    def __init__(self):
        self.instructions = []

    def compile(self, ast):
        for stmt in ast:
            self.visit(stmt)
        return self.instructions

    def emit(self, opcode, arg=None):
        self.instructions.append({'op': opcode, 'arg': arg})
        return len(self.instructions) - 1

    def visit(self, node):
        if node[0] == 'VAR_DECL' or node[0] == 'ASSIGN':
            self.visit(node[2])
            self.emit('STORE', node[1])
        elif node[0] == 'PRINT':
            self.visit(node[1])
            self.emit('PRINT')
        elif node[0] == 'IF':
            self.visit(node[1])
            jmp_idx = self.emit('JMP_FALSE') # Placeholder
            for stmt in node[2]:
                self.visit(stmt)
            self.instructions[jmp_idx]['arg'] = len(self.instructions) # Backpatch
        elif node[0] == 'WHILE':
            start_idx = len(self.instructions)
            self.visit(node[1])
            jmp_idx = self.emit('JMP_FALSE') # Placeholder
            for stmt in node[2]:
                self.visit(stmt)
            self.emit('JMP', start_idx)
            self.instructions[jmp_idx]['arg'] = len(self.instructions) # Backpatch
        elif node[0] == 'BIN_OP':
            self.visit(node[2])
            self.visit(node[3])
            self.emit('BIN_OP', node[1])
        elif node[0] == 'NUM' or node[0] == 'STR' or node[0] == 'BOOL':
            self.emit('PUSH', node[1])
        elif node[0] == 'VAR':
            self.emit('LOAD', node[1])

# --- 4. MÁQUINA VIRTUAL (INTÉRPRETE DE BYTECODE) ---
# Ejecuta las instrucciones generadas

class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.env = {}

    def run(self, bytecode):
        pc = 0
        while pc < len(bytecode):
            inst = bytecode[pc]
            op = inst['op']
            arg = inst['arg']

            if op == 'PUSH':
                self.stack.append(arg)
            elif op == 'STORE':
                self.env[arg] = self.stack.pop()
            elif op == 'LOAD':
                if arg not in self.env:
                    raise NameError(f"Variable '{arg}' no definida.")
                self.stack.append(self.env[arg])
            elif op == 'PRINT':
                print(self.stack.pop())
            elif op == 'BIN_OP':
                b = self.stack.pop()
                a = self.stack.pop()
                if arg == '+': self.stack.append(a + b)
                elif arg == '-': self.stack.append(a - b)
                elif arg == '*': self.stack.append(a * b)
                elif arg == '/': self.stack.append(a / b)
                elif arg == '==': self.stack.append(a == b)
                elif arg == '!=': self.stack.append(a != b)
                elif arg == '<': self.stack.append(a < b)
                elif arg == '>': self.stack.append(a > b)
                elif arg == '<=': self.stack.append(a <= b)
                elif arg == '>=': self.stack.append(a >= b)
            elif op == 'JMP_FALSE':
                cond = self.stack.pop()
                if not cond:
                    pc = arg
                    continue
            elif op == 'JMP':
                pc = arg
                continue
            
            pc += 1

# --- 5. INTERFAZ DE LÍNEA DE COMANDOS (CLI) ---

def print_banner():
    print("=" * 60)
    print(" LATINCHAIN CODE COMPILER & VM ")
    print(" Creado por: Lcdo. César Cordero ")
    print(" Licencia: GNU GPLv3 ")
    print(" Plataforma Multiplataforma (Web/Desktop/Server/Mobile) ")
    print("=" * 60)

def main():
    if len(sys.argv) < 3:
        print_banner()
        print("\nUso:")
        print("  python3 latinchain.py run archivo.la    (Interpretar código fuente)")
        print("  python3 latinchain.py compile archivo.la (Compilar a ejecutable .lac)")
        print("  python3 latinchain.py exec archivo.lac  (Ejecutar binario compilado)")
        sys.exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command == "run":
        if not filename.endswith('.la'):
            print("Error: El código fuente debe tener extensión .la")
            sys.exit(1)
        
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Flujo completo
        lexer = Lexer(source)
        parser = Parser(lexer.tokens)
        ast = parser.parse()
        compiler = Compiler()
        bytecode = compiler.compile(ast)
        
        vm = VirtualMachine()
        vm.run(bytecode)

    elif command == "compile":
        if not filename.endswith('.la'):
            print("Error: El código fuente debe tener extensión .la")
            sys.exit(1)
        
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        lexer = Lexer(source)
        parser = Parser(lexer.tokens)
        ast = parser.parse()
        compiler = Compiler()
        bytecode = compiler.compile(ast)
        
        out_filename = filename.replace('.la', '.lac')
        with open(out_filename, 'wb') as f:
            pickle.dump(bytecode, f)
            
        print(f"Compilación exitosa. Ejecutable creado: {out_filename}")

    elif command == "exec":
        if not filename.endswith('.lac'):
            print("Error: El ejecutable debe tener extensión .lac")
            sys.exit(1)
        
        with open(filename, 'rb') as f:
            bytecode = pickle.load(f)
            
        vm = VirtualMachine()
        vm.run(bytecode)
        
    else:
        print("Comando no reconocido. Usa: run, compile o exec.")

if __name__ == '__main__':
    main()
