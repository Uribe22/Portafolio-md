class AsignaturaManager:
    def __init__(self):
        self.asignaturas_db = {}

    def crear_asignatura(self, asignatura):
        if asignatura.codigo in self.asignaturas_db:
            print(f"[ERROR] La asignatura {asignatura.codigo} ya existe.")
        else:
            self.asignaturas_db[asignatura.codigo] = asignatura
            print(f"[CREAR] Asignatura {asignatura.nombre} creada.")

    def recuperar_asignatura(self, codigo):
        asignatura = self.asignaturas_db.get(codigo)
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
        if codigo in self.asignaturas_db:
            del self.asignaturas_db[codigo]
            print(f"[ELIMINAR] Asignatura {codigo} eliminada.")
        else:
            print(f"[ERROR] Asignatura {codigo} no encontrada.")
