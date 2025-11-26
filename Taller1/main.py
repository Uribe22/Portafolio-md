from models.alumno import EstudianteAyudante, EstudianteDoctorado, EstudianteNoAyudante, EstudianteMagister, Alumni
from managers.alumno_manager import AlumnoManager
from managers.asignatura_manager import AsignaturaManager
from models.asignatura import Asignatura

if __name__ == "__main__":
    alumno_manager = AlumnoManager()
    asignatura_manager = AsignaturaManager()

    # Crear asignaturas
    asignatura_manager.crear_asignatura(Asignatura("Metodología de Diseño", "ICI414", 4, "Pregrado"))
    asignatura_manager.crear_asignatura(Asignatura("Lenguaje y Autómatas", "ICI413", 5, "Doctorado"))

    # Crear alumnos
    alumno1 = EstudianteAyudante("Andrés González", 20, "12.345.678-9", "2001-10-28")
    alumno2 = EstudianteDoctorado("Lorena Uribe", 30, "9.876.543-2", "2001-11-02")
    alumno3 = EstudianteNoAyudante("Carlos Soto", 22, "11.222.333-4", "2001-06-15")
    alumno4 = EstudianteMagister("Paula Díaz", 28, "15.555.666-7", "1996-03-08")
    alumno5 = Alumni("Javier Reyes", 35, "10.000.111-2", "1988-01-12")

    # Crear alumnos en la base de datos
    alumno_manager.crear_alumno(alumno1)
    alumno_manager.crear_alumno(alumno2)
    alumno_manager.crear_alumno(alumno3)
    alumno_manager.crear_alumno(alumno4)
    alumno_manager.crear_alumno(alumno5)

    # Agregar asignaturas a los alumnos
    asignatura1 = asignatura_manager.recuperar_asignatura("ICI414")
    asignatura2 = asignatura_manager.recuperar_asignatura("ICI413")
    
    alumno1.agregar_asignatura(asignatura1)
    alumno2.agregar_asignatura(asignatura2)
    alumno3.agregar_asignatura(asignatura1)
    alumno4.agregar_asignatura(asignatura2)

    # Descargar notas
    alumno1.descargar_notas()
    alumno2.descargar_notas()
    alumno3.descargar_notas()
    alumno4.descargar_notas()
    alumno5.descargar_notas()

    # Realizar actividades
    alumno1.actividades()
    alumno1.hacer_ayudantia()
    
    alumno2.actividades()
    alumno2.investigar()
    alumno2.hacer_clases()
    
    alumno3.actividades()
    alumno3.estudiar()

    alumno4.actividades()
    alumno4.estudiar()
    alumno4.hacer_clases()

    alumno5.actividades()
    
    # Modificar, eliminar y recuperar alumnos
    alumno_manager.modificar_alumno("12.345.678-9", edad=21)
    alumno_manager.eliminar_alumno("10.000.111-2")
    asignatura_manager.modificar_asignatura("ICI414", creditos=5)
    alumno_manager.recuperar_alumno("12.345.678-9")
    alumno_manager.recuperar_alumno("10.000.111-2")
    asignatura_manager.recuperar_asignatura("ICI414")
    asignatura_manager.recuperar_asignatura("ICI413")
    asignatura_manager.eliminar_asignatura("ICI413")
