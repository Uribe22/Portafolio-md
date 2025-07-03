# Taller 1 - Principios SOLID

## Descripción
Este taller corresponde al desarrollo de un sistema simulado de gestión de alumnos y asignaturas utilizando los principios SOLID, como parte del portafolio de la asignatura **Metodología de Diseño**.

Se implementan clases para diferentes tipos de alumnos (Titulados, Estudiantes de Pregrado, Magíster, Doctorado, etc.) y se simula el manejo de asignaturas, actividades académicas y notas, todo mediante una base de datos representada por diccionarios en Python.

## Supuestos
- **No se usa una base de datos real**: se simula con diccionarios (`alumnos_db` y `asignaturas_db`).
- **Datos de notas**: todas las asignaturas se agregan inicialmente con nota `None` (sin nota).
- **Acciones de los estudiantes**: los métodos de actividades (por ejemplo, `estudiar`, `hacer_clases`, `investigar`) muestran un mensaje en consola, no realizan procesos reales.
- **Control de acceso**: no se implementa un sistema de usuarios ni permisos.
- **Validación mínima**: el sistema no valida si la asignatura es adecuada al nivel del estudiante.
- **Eliminación y modificación**: los métodos de eliminación y modificación operan directamente sobre los diccionarios sin confirmación adicional.

## Cómo ejecutar
1. Abre una terminal en la carpeta del archivo.
2. Ejecuta con: python "Taller 1.py" 

## Integrantes
- **Andrés González** - 20.907.791-4  
- **Lorena Uribe** - 20.908.387-6
