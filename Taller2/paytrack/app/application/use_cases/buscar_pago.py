# app/application/use_cases/buscar_pago.py
from app.application.services.pago_service import PagoService

def buscar_pago(nombre_cliente: str, pago_service: PagoService):
    return pago_service.buscar_pagos_por_cliente(nombre_cliente)
