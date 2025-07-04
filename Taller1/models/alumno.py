from abc import ABC, abstractmethod

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
            print(f"- {asignatura.nombre} ({asignatura.codigo}): {nota if nota else 'Sin nota'}")

    @abstractmethod
    def actividades(self):
        pass

    def __str__(self):
        return f"{self.nombre} - {self.rut} - {type(self).__name__}"


class EstudianteNoAyudante(Alumno):
    def actividades(self):
        print(f"{self.nombre} (No Ayudante): Estudia.")

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")


class EstudianteAyudante(Alumno):
    def actividades(self):
        print(f"{self.nombre} (Ayudante): Estudia y hace ayudantías.")

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

    def hacer_ayudantia(self):
        print(f"{self.nombre} está haciendo una ayudantía.")


class EstudianteMagister(Alumno):
    def actividades(self):
        print(f"{self.nombre} (Magister): Estudia y hace clases.")

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

    def hacer_clases(self):
        print(f"{self.nombre} está haciendo clases.")


class EstudianteDoctorado(Alumno):
    def actividades(self):
        print(f"{self.nombre} (Doctorado): Estudia, hace clases e investiga.")

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

    def hacer_clases(self):
        print(f"{self.nombre} está haciendo clases.")

    def investigar(self):
        print(f"{self.nombre} está investigando.")


class Alumni(Alumno):
    def actividades(self):
        print(f"{self.nombre} (Titulado): No realiza actividades académicas.")
