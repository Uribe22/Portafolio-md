import uuid
from datetime import datetime

class Pago:
    def __init__(self, nombre_cliente: str, monto: float, estado: str = "COMPLETADO", fecha=None):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        
        # Asignar un ID único con uuid
        self.id = str(uuid.uuid4())  # Genera un ID único para cada pago
        self.nombre_cliente = nombre_cliente
        self.monto = monto
        self.estado = estado
        self.fecha = fecha if fecha else datetime.now()

    def to_dict(self):
        """Convertir el objeto a un diccionario para la respuesta API."""
        return {
            "id": self.id,  # Añadir el ID en la representación del pago
            "nombre_cliente": self.nombre_cliente,
            "monto": self.monto,
            "estado": self.estado,
            "fecha": self.fecha.isoformat(),
        }
