# app/application/services/pago_service.py
from app.core.models.pago import Pago

class PagoService:
    def __init__(self, repository):
        self.repository = repository

    def registrar_pago(self, nombre_cliente: str, monto: float):
        """Registrar un nuevo pago."""
        pago = Pago(nombre_cliente, monto)
        self.repository.save(pago)
        return pago

    def listar_pagos(self):
        """Listar todos los pagos."""
        return self.repository.get_all()

    def buscar_pagos_por_cliente(self, nombre_cliente: str):
        """Buscar pagos por nombre de cliente."""
        return self.repository.get_by_cliente(nombre_cliente)

    def eliminar_pago(self, pago_id: int):
        """Eliminar un pago por ID."""
        pago = self.repository.get_by_id(pago_id)
        if not pago:
            raise ValueError("Pago no encontrado.")
        if pago.estado != "COMPLETADO":
            raise ValueError("Solo los pagos COMPLETADOS pueden ser eliminados.")
        self.repository.delete(pago)
