# Taller 1 - Principios SOLID

## Descripción
Este taller corresponde al desarrollo de un sistema simulado de gestión de alumnos y asignaturas utilizando los principios **SOLID**, como parte del portafolio de la asignatura **Metodología de Diseño**.

Se implementan clases para diferentes tipos de alumnos (Titulados, Estudiantes de Pregrado, Magíster, Doctorado, etc.) y se simula el manejo de asignaturas, actividades académicas y notas, todo mediante una base de datos representada por diccionarios en Python.

### Principios SOLID Implementados:
- **S** - Responsabilidad Única
- **O** - Abierto/Cerrado
- **L** - Sustitución de Liskov
- **I** - Segregación de Interfaces
- **D** - Inversión de Dependencias

## Supuestos
- **No se usa una base de datos real**: Se simula con diccionarios (`alumnos_db` y `asignaturas_db`).
- **Datos de notas**: Todas las asignaturas se agregan inicialmente con la nota `None` (sin nota).
- **Acciones de los estudiantes**: Los métodos de actividades (por ejemplo, `estudiar`, `hacer_clases`, `investigar`) muestran un mensaje en consola, pero no realizan procesos reales.
- **Control de acceso**: No se implementa un sistema de usuarios ni permisos.
- **Validación mínima**: El sistema no valida si la asignatura es adecuada al nivel del estudiante.
- **Eliminación y modificación**: Los métodos de eliminación y modificación operan directamente sobre los diccionarios sin confirmación adicional.

## Estructura del Proyecto
- **models/**: Contiene las clases `Alumno` y `Asignatura`.
- **managers/**: Contiene las clases para gestionar alumnos (`AlumnoManager`) y asignaturas (`AsignaturaManager`).
- **main.py**: El archivo principal que ejecuta el código.

## Cómo ejecutar

1. Abre una terminal en la carpeta del archivo.
2. Ejecuta el script con el siguiente comando:

   ```bash
   python main.py

## Integrantes
- **Andrés González** - 20.907.791-4  
- **Lorena Uribe** - 20.908.387-6
