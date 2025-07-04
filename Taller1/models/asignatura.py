# models/asignatura.py
class Asignatura:
    def __init__(self, nombre, codigo, creditos, nivel):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.nivel = nivel  # Pregrado, Magister, Doctorado

    def __str__(self):
        return f"{self.nombre} ({self.codigo}) - {self.creditos} créditos - {self.nivel}"
