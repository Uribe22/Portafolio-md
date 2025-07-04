# app/application/use_cases/registrar_pago.py
from app.application.services.pago_service import PagoService

def registrar_pago(nombre_cliente: str, monto: float, pago_service: PagoService):
    return pago_service.registrar_pago(nombre_cliente, monto)
