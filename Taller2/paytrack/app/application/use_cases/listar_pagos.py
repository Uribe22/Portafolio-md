# app/application/use_cases/listar_pagos.py
from app.application.services.pago_service import PagoService

def listar_pagos(pago_service: PagoService):
    return pago_service.listar_pagos()
