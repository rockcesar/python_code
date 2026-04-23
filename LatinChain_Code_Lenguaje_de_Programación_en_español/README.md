LatinChain Code 🚀

LatinChain Code es un lenguaje de programación multiplataforma, interpretado y compilado a bytecode, diseñado completamente con sintaxis en español. Fue creado con el propósito de ser una herramienta intuitiva y accesible para hispanohablantes, permitiendo escribir algoritmos de forma natural y clara.

Creador: Lcdo. César Cordero.

Licencia: GNU GPLv3.

Basado en: Python 3 (Máquina Virtual y Compilador).

INSTRUCCIONES DE USO (Requiere latinchain.py):
1. Interpretar al vuelo:

python3 latinchain.py run fibonacci.la

2. Compilar a binario:

python3 latinchain.py compile fibonacci.la

3. Ejecutar binario:

python3 latinchain.py exec fibonacci.lac

✨ Características Principales

🗣️ Sintaxis en Español: Palabras reservadas como variable, si, mientras, imprimir, verdadero y falso.

⚡ Ejecución Directa (Intérprete): Capacidad de leer y ejecutar código fuente (archivos .la) al vuelo.

📦 Compilación a Bytecode: Permite compilar el código fuente a archivos binarios ejecutables (archivos .lac) para proteger el código original y agilizar cargas.

🌍 Multiplataforma: Al ejecutarse sobre su propia Máquina Virtual (VM) implementada en Python, corre perfectamente en Windows, Linux, macOS, Servidores, y es adaptable a web o móviles.

⌨️ Tipado Dinámico: Inferencia automática de tipos (Números, Cadenas, Booleanos).

🛠️ Requisitos e Instalación

Para hacer funcionar el motor de LatinChain Code, solo necesitas tener instalado Python 3.x en tu sistema.

Clona este repositorio:

git clone [https://github.com/rockcesar/python_code.git](https://github.com/rockcesar/python_code.git)

cd python_code/LatinChain_Code_Lenguaje_de_Programación_en_español


Asegúrate de tener el archivo principal del motor: latinchain.py.

💻 Guía de Uso Rápido

El motor CLI (Interfaz de Línea de Comandos) de LatinChain Code soporta tres operaciones principales:

1. Interpretar código fuente directamente (run)

Ejecuta un archivo .la sin compilarlo previamente.

python3 latinchain.py run mi_programa.la


2. Compilar a binario (compile)

Convierte un archivo .la en un archivo de bytecode con extensión .lac.

python3 latinchain.py compile mi_programa.la


3. Ejecutar binario compilado (exec)

Ejecuta un archivo .lac generado por el compilador.

python3 latinchain.py exec mi_programa.lac


📖 Ejemplo de Código

El siguiente es un ejemplo de un programa escrito en LatinChain Code que calcula la secuencia de Fibonacci. Puedes encontrar este ejemplo en el archivo fibonacci.la.

// Programa: Secuencia de Fibonacci
// Escrito en LatinChain Code

imprimir("--- SECUENCIA DE FIBONACCI ---");

variable limite = 100;

variable a = 0;

variable b = 1;

variable siguiente = 0;

imprimir(a);

imprimir(b);

siguiente = a + b;

mientras (siguiente <= limite) {
    
    imprimir(siguiente);
    
    a = b;
    
    b = siguiente;
    
    siguiente = a + b;
}

imprimir("Programa finalizado con exito.");


📜 Sintaxis Básica

Comentarios: Utiliza // para comentarios de una línea.

Variables: Declaradas con la palabra variable. (Ej. variable x = 10;). Todas las sentencias deben terminar con punto y coma ;.

Imprimir: Muestra en consola utilizando imprimir(valor);.

Condicionales: Estructura si (condicion) { ... }.

Ciclos: Bucle mientras (condicion) { ... }.

Operadores: +, -, *, /, ==, !=, <, >, <=, >=.

🤝 Contribuir

¡Las contribuciones son bienvenidas! Si deseas mejorar el analizador léxico, añadir nuevas funciones al compilador o extender la máquina virtual, siéntete libre de hacer un Fork del repositorio y enviar un Pull Request.

📄 Licencia

Este proyecto es Software Libre y se distribuye bajo los términos de la GNU General Public License v3.0 (GPLv3). Puedes redistribuirlo y/o modificarlo de acuerdo con la licencia de la Free Software Foundation.
