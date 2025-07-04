# tests/test_pagos.py
import pytest
from app.core.models.pago import Pago
from app.adapters.repositories.pago_repository import PagoRepository
from app.application.services.pago_service import PagoService
from app.application.use_cases.registrar_pago import registrar_pago
from app.application.use_cases.listar_pagos import listar_pagos
from app.application.use_cases.buscar_pago import buscar_pago
from app.application.use_cases.eliminar_pago import eliminar_pago

# Limpiar el repositorio antes de cada prueba
@pytest.fixture(autouse=True)
def setup_and_teardown():
    global pago_repository
    global pago_service
    pago_repository = PagoRepository()
    pago_service = PagoService(pago_repository)
    pago_repository.pagos.clear()  # Limpiar la lista de pagos antes de cada prueba
    yield  # Continuar con la prueba
    # No es necesario limpiar nada después, ya que se limpia antes de cada prueba

def test_registrar_pago():
    pago = registrar_pago("Juan Perez", 100.0, pago_service)
    assert pago.nombre_cliente == "Juan Perez"
    assert pago.monto == 100.0
    assert pago.estado == "COMPLETADO"

def test_listar_pagos():
    registrar_pago("Juan Perez", 100.0, pago_service)
    registrar_pago("Maria Lopez", 150.0, pago_service)
    pagos = listar_pagos(pago_service)
    assert len(pagos) == 2

def test_buscar_pago_por_cliente():
    registrar_pago("Juan Perez", 100.0, pago_service)
    registrar_pago("Juan Perez", 150.0, pago_service)
    pagos = buscar_pago("Juan Perez", pago_service)
    assert len(pagos) == 2

def test_eliminar_pago():
    pago = registrar_pago("Juan Perez", 100.0, pago_service)
    pago_id = pago.id  # Usamos el ID correcto
    eliminar_pago(pago_id=pago_id, pago_service=pago_service)
    pagos = listar_pagos(pago_service)
    assert len(pagos) == 0  # Verifica que la lista de pagos esté vacía
