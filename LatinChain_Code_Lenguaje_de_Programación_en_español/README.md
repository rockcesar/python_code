LatinChain Code 🚀

LatinChain Code es un lenguaje de programación multiplataforma, interpretado y compilado a bytecode, diseñado completamente con sintaxis en español. Fue creado con el propósito de ser una herramienta intuitiva y accesible para hispanohablantes, permitiendo escribir algoritmos de forma natural y clara.

Creador: Lcdo. César Cordero

Licencia: GNU GPLv3

Basado en: Python 3 (Máquina Virtual y Compilador)

✨ Características Principales

🗣️ Sintaxis en Español: Palabras reservadas como variable, si, mientras, imprimir, verdadero, falso e importar.

🌎 Soporte UTF-8 Nativo: Permite el uso de caracteres especiales del español (como la ñ y las vocales acentuadas) tanto en cadenas de texto como en nombres de variables y funciones.

🧩 Sistema de Módulos Avanzado: Divide y organiza tu código en múltiples archivos y carpetas. El motor entiende el contexto del directorio actual y soporta importaciones mediante rutas relativas (./, ../), absolutas (/) y el uso de comodines y prefijos (*).

⚡ Ejecución Directa (Intérprete): Capacidad de leer y ejecutar código fuente (archivos .la) al vuelo.

📦 Compilación a Bytecode: Permite compilar el código fuente a archivos binarios ejecutables (archivos .lac) para proteger el código original y agilizar cargas. Al compilar, todos los módulos importados se resuelven y empaquetan en un solo archivo binario.

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

    python latinchain.py run mi_programa.la


2. Compilar a binario (compile)

Convierte un archivo .la en un archivo de bytecode con extensión .lac.

    python latinchain.py compile mi_programa.la


3. Ejecutar binario compilado (exec)

Ejecuta un archivo .lac generado por el compilador.

    python latinchain.py exec mi_programa.lac


🧩 Uso de Módulos (Importaciones)

LatinChain Code te permite organizar tu proyecto de forma profesional. Para incluir el código de otro archivo .la, utiliza la palabra reservada importar seguida del nombre del archivo o su ruta (sin la extensión).

Importación en el mismo directorio:

    importar matematicas

    imprimir(pi);


Importación usando rutas relativas y absolutas:
El motor es capaz de navegar por tu sistema de archivos partiendo de la ubicación del script actual o leyendo la ruta absoluta.

    // Desde una subcarpeta actual
    importar ./utilidades/textos

    // Desde un directorio superior
    importar ../modulos/core/sistema

    // Desde una ruta absoluta en el sistema operativo
    importar /home/usuario1/matematicas/maths


Importación masiva con Comodines y Prefijos (*):
Si deseas cargar múltiples módulos a la vez, puedes usar el comodín *. También puedes combinarlo con un prefijo para cargar solo los archivos que comiencen con una palabra específica en ese directorio.

    // Importar absolutamente todos los archivos .la de la carpeta actual
    importar ./*

    // Importar todos los archivos .la de un directorio superior
    importar ../matematicas/*

    // Importar SOLO los archivos que comiencen con "maths" (ej. maths1.la, maths_avanzadas.la)
    importar ./maths*

    // Importar por prefijo desde una ruta absoluta
    importar /home/usuario1/utilidades/core_*


Nota: Al compilar el archivo principal, el compilador de LatinChain buscará en las rutas indicadas e incluirá automáticamente el código de todos los módulos encontrados dentro del binario final .lac.

📖 Ejemplo de Código (Fibonacci)

El siguiente es un ejemplo de un programa escrito en LatinChain Code que calcula la secuencia de Fibonacci utilizando un bucle mientras.

    // Programa: Secuencia de Fibonacci
    // Escrito en LatinChain Code

    imprimir("--- SECUENCIA DE FIBONACCI ---");

    variable límite = 100;
    variable a = 0;
    variable b = 1;
    variable siguiente = 0;

    imprimir(a);
    imprimir(b);

    siguiente = a + b;

    mientras (siguiente <= límite) {
        imprimir(siguiente);
        a = b;
        b = siguiente;
        siguiente = a + b;
    }

    imprimir("Programa finalizado con éxito.");


📜 Sintaxis Básica

Comentarios: Utiliza // para comentarios de una línea.

Variables: Declaradas con la palabra variable. (Ej. variable año_actual = 2026;). La mayoría de las sentencias deben terminar con punto y coma ;.

Importar: Incluye archivos externos usando importar ruta/del/modulo o utilidades masivas como importar ./prefijo* (el ; al final es opcional).

Imprimir: Muestra en consola utilizando imprimir(valor);.

Condicionales: Estructura si (condición) { ... }.

Ciclos: Bucle mientras (condición) { ... }.

Operadores: +, -, *, /, ==, !=, <, >, <=, >=.

🤝 Contribuir

¡Las contribuciones son bienvenidas! Si deseas mejorar el analizador léxico, añadir nuevas funciones al compilador o extender la máquina virtual, siéntete libre de hacer un Fork del repositorio y enviar un Pull Request.

📄 Licencia

Este proyecto es Software Libre y se distribuye bajo los términos de la GNU General Public License v3.0 (GPLv3). Puedes redistribuirlo y/o modificarlo de acuerdo con la licencia de la Free Software Foundation.
