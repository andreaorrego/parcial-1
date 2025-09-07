ANÁLISIS DE SUELOS EN COLOMBIA - PARCIAL 1

Este proyecto corresponde al Parcial 1 de Fundamentos Básicos de Python.
Consiste en una aplicación de escritorio y línea de comandos que permite consultar información del archivo Resultados de Análisis
de Laboratorio Suelos en Colombia, con el fin de facilitar la interpretación de variables edáficas asociadas a diferentes cultivos.

FUNCIONALIDADES
- Permite al usuario ingresar: Departamento, Municipio, Cultivo y cantidad de registros a consultar.
- Genera tablas con información sobre: Departamento, Municipio, Cultivo, Topografía
- Valores estadísticos como las medianas de pH, Fósforo y Potasio
- En el caso de Risaralda: también Aluminio, Calcio, Sodio y Zinc
- Incluye funciones adicionales que muestran al usuario los municipios disponibles por departamento y los cultivos asociados a cada municipio.

ARQUITECTURA DEL PROYECTO
- El sistema se desarrolló bajo un enfoque modular:
- ui.py → Interacción con el usuario (entrada de datos por consola).
- api.py → Procesamiento y filtrado de datos con pandas.
- main.py → Punto de entrada que coordina la ejecución.
- Archivo CSV → Fuente principal de datos para el análisis.

EJECUCIÓN
- Clona este repositorio:
  git clone https://github.com/andreaorrego/parcial-1.git
  cd parcial-1

- Instala las dependencias necesarias:
  pip install pandas

- Ejecuta el programa:
  python main.py

EVIDENCIAS
- Interacción con el usuario en consola (ingreso de datos).
- Tablas de salida con los resultados solicitados.
- Repositorio con trazabilidad en GitHub.

CONCLUSIONES
- Se cumplieron los requerimientos funcionales y arquitectónicos.
- La modularización facilitó la comprensión y el mantenimiento del código.
- El proyecto refuerza conceptos básicos de programación en Python.
- Se generó una herramienta práctica y aplicable al ámbito agrícola.
