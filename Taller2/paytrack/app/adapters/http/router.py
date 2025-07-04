# app/adapters/http/router.py
from fastapi import APIRouter, HTTPException
from app.application.use_cases.registrar_pago import registrar_pago
from app.application.use_cases.listar_pagos import listar_pagos
from app.application.use_cases.buscar_pago import buscar_pago
from app.application.use_cases.eliminar_pago import eliminar_pago
from app.application.services.pago_service import PagoService
from app.adapters.repositories.pago_repository import PagoRepository

router = APIRouter()

# Inicializar repositorio y servicio
pago_repository = PagoRepository()
pago_service = PagoService(pago_repository)

@router.post("/pagos")
async def registrar_pago_endpoint(nombre_cliente: str, monto: float):
    try:
        pago = registrar_pago(nombre_cliente, monto, pago_service)
        return pago.to_dict(), 201
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/pagos")
async def listar_pagos_endpoint():
    pagos = listar_pagos(pago_service)
    return [pago.to_dict() for pago in pagos]

@router.get("/pagos/{nombre_cliente}")
async def buscar_pagos_por_cliente_endpoint(nombre_cliente: str):
    pagos = buscar_pago(nombre_cliente, pago_service)
    return [pago.to_dict() for pago in pagos]

@router.delete("/pagos/{pago_id}")
async def eliminar_pago_endpoint(pago_id: int):
    try:
        eliminar_pago(pago_id, pago_service)
        return {}, 204
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
