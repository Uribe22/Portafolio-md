#Andés González, 20.907.791-4
#Lorena Uribe, 20.908.387-6

from abc import ABC, abstractmethod

# Simulación de base de datos
alumnos_db = {}
asignaturas_db = {}


class Asignatura:
    def __init__(self, nombre, codigo, creditos, nivel):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.nivel = nivel  # Pregrado, Magister, Doctorado

    def __str__(self):
        return f"{self.nombre} ({self.codigo}) - {self.creditos} créditos - {self.nivel}"


class Alumno(ABC):
    def __init__(self, nombre, edad, rut, fecha_nacimiento):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.asignaturas = []
        self.notas = {}

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
        self.notas[asignatura.codigo] = None
        print(f"[INFO] Asignatura {asignatura} agregada para {self.nombre}")

    def descargar_notas(self):
        print(f"[NOTAS] {self.nombre}:")
        for asignatura in self.asignaturas:
            nota = self.notas.get(asignatura.codigo)
            nota_str = nota if nota is not None else "Sin nota"
            print(f"- {asignatura.nombre} ({asignatura.codigo}): {nota_str}")

    @abstractmethod
    def actividades(self):
        pass

    def __str__(self):
        return f"{self.nombre} - {self.rut} - {type(self).__name__}"


class Estudiante(ABC):
    @abstractmethod
    def estudiar(self):
        pass

class Profesor(ABC):
    @abstractmethod
    def hacer_clases(self):
        pass


# Subclases de alumnos
class Alumni(Alumno):
    def actividades(self):
        print(f"{self.nombre} (Titulado): No realiza actividades académicas.")

class EstudianteNoAyudante(Alumno, Estudiante):
    def actividades(self):
        print(f"{self.nombre} (No Ayudante): Estudia.")
        
    def estudiar(self):
        print(f"{self.nombre} está estudiando")


class EstudianteAyudante(Alumno, Estudiante):
    def actividades(self):
        print(f"{self.nombre} (Ayudante): Estudia y hace ayudantías.")
        
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

    def hacer_ayudantia(self):
        print(f"{self.nombre} está haciendo una ayudantía.")


class EstudianteMagister(Alumno, Estudiante, Profesor):
    def actividades(self):
        print(f"{self.nombre} (Magister): Estudia y hace clases.")
        
    def estudiar(self):
        print(f"{self.nombre} está estudiando")
        
    def hacer_clases(self):
        print(f"{self.nombre} está haciendo clases")


class EstudianteDoctorado(Alumno, Estudiante, Profesor):
    def actividades(self):
        print(f"{self.nombre} (Doctorado): Estudia, hace clases e investiga.")

    def estudiar(self):
        print(f"{self.nombre} está estudiando")

    def hacer_clases(self):
        print(f"{self.nombre} está haciendo clases")

    def investigar(self):
        print(f"{self.nombre} está investigando")


class AlumnoManager:
    def crear_alumno(self, alumno):
        if alumno.rut in alumnos_db:
            print(f"[ERROR] El alumno {alumno.rut} ya existe.")
        else:
            alumnos_db[alumno.rut] = alumno
            print(f"[CREAR] Alumno {alumno.nombre} creado.")

    def recuperar_alumno(self, rut):
        alumno = alumnos_db.get(rut)
        if alumno:
            print(f"[RECUPERAR] {alumno}")
            return alumno
        else:
            print(f"[ERROR] Alumno {rut} no encontrado.")
            return None

    def modificar_alumno(self, rut, **kwargs):
        alumno = self.recuperar_alumno(rut)
        if alumno:
            for key, value in kwargs.items():
                if hasattr(alumno, key):
                    setattr(alumno, key, value)
                    print(f"[MODIFICAR] {key} actualizado a {value}.")

    def eliminar_alumno(self, rut):
        if rut in alumnos_db:
            del alumnos_db[rut]
            print(f"[ELIMINAR] Alumno {rut} eliminado.")
        else:
            print(f"[ERROR] Alumno {rut} no encontrado.")


class AsignaturaManager:
    def crear_asignatura(self, asignatura):
        if asignatura.codigo in asignaturas_db:
            print(f"[ERROR] La asignatura {asignatura.codigo} ya existe.")
        else:
            asignaturas_db[asignatura.codigo] = asignatura
            print(f"[CREAR] Asignatura {asignatura.nombre} creada.")

    def recuperar_asignatura(self, codigo):
        asignatura = asignaturas_db.get(codigo)
        if asignatura:
            print(f"[RECUPERAR] {asignatura}")
            return asignatura
        else:
            print(f"[ERROR] Asignatura {codigo} no encontrada.")
            return None

    def modificar_asignatura(self, codigo, **kwargs):
        asignatura = self.recuperar_asignatura(codigo)
        if asignatura:
            for key, value in kwargs.items():
                if hasattr(asignatura, key):
                    setattr(asignatura, key, value)
                    print(f"[MODIFICAR] {key} actualizado a {value}.")

    def eliminar_asignatura(self, codigo):
        if codigo in asignaturas_db:
            del asignaturas_db[codigo]
            print(f"[ELIMINAR] Asignatura {codigo} eliminada.")
        else:
            print(f"[ERROR] Asignatura {codigo} no encontrada.")


if __name__ == "__main__":
    alumno_manager = AlumnoManager()
    asignatura_manager = AsignaturaManager()

    asignatura_manager.crear_asignatura(Asignatura("Metodología de Diseño", "ICI414", 4, "Pregrado"))
    asignatura_manager.crear_asignatura(Asignatura("Lenguaje y Autómatas", "ICI413", 5, "Doctorado"))

    alumno1 = EstudianteAyudante("Andrés González", 20, "12.345.678-9", "2001-10-28")
    alumno2 = EstudianteDoctorado("Lorena Uribe", 30, "9.876.543-2", "2001-11-02")
    alumno3 = EstudianteNoAyudante("Carlos Soto", 22, "11.222.333-4", "2001-06-15")
    alumno4 = EstudianteMagister("Paula Díaz", 28, "15.555.666-7", "1996-03-08")
    alumno5 = Alumni("Javier Reyes", 35, "10.000.111-2", "1988-01-12")


    alumno_manager.crear_alumno(alumno1)
    alumno_manager.crear_alumno(alumno2)
    alumno_manager.crear_alumno(alumno3)
    alumno_manager.crear_alumno(alumno4)
    alumno_manager.crear_alumno(alumno5)

    asignatura1 = asignaturas_db["ICI414"]
    asignatura2 = asignaturas_db["ICI413"]
    
    alumno1.agregar_asignatura(asignatura1)
    alumno2.agregar_asignatura(asignatura2)
    alumno3.agregar_asignatura(asignatura1)
    alumno4.agregar_asignatura(asignatura2)

    alumno1.descargar_notas()
    alumno2.descargar_notas()
    alumno3.descargar_notas()
    alumno4.descargar_notas()
    alumno5.descargar_notas()

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
    
    alumno_manager.modificar_alumno("12.345.678-9", edad=21)
    alumno_manager.eliminar_alumno("10.000.111-2")
    asignatura_manager.modificar_asignatura("ICI414", creditos=5)
    alumno_manager.recuperar_alumno("12.345.678-9")
    alumno_manager.recuperar_alumno("10.000.111-2")
    asignatura_manager.recuperar_asignatura("ICI414")
    asignatura_manager.recuperar_asignatura("ICI413")
    asignatura_manager.eliminar_asignatura("ICI413")
