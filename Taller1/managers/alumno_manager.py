class AlumnoManager:
    def __init__(self):
        self.alumnos_db = {}

    def crear_alumno(self, alumno):
        if alumno.rut in self.alumnos_db:
            print(f"[ERROR] El alumno {alumno.rut} ya existe.")
        else:
            self.alumnos_db[alumno.rut] = alumno
            print(f"[CREAR] Alumno {alumno.nombre} creado.")

    def recuperar_alumno(self, rut):
        alumno = self.alumnos_db.get(rut)
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
        if rut in self.alumnos_db:
            del self.alumnos_db[rut]
            print(f"[ELIMINAR] Alumno {rut} eliminado.")
        else:
            print(f"[ERROR] Alumno {rut} no encontrado.")
