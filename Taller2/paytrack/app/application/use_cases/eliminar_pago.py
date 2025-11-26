# app/application/use_cases/eliminar_pago.py
from app.application.services.pago_service import PagoService

def eliminar_pago(pago_id: int, pago_service: PagoService):
    return pago_service.eliminar_pago(pago_id)
