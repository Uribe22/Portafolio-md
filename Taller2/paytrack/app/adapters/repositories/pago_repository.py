# app/adapters/repositories/pago_repository.py
class PagoRepository:
    def __init__(self):
        self.pagos = []  # En memoria

    def save(self, pago):
        """Guardar el pago."""
        self.pagos.append(pago)

    def get_all(self):
        """Obtener todos los pagos."""
        return self.pagos

    def get_by_cliente(self, nombre_cliente):
        """Buscar pagos por cliente."""
        return [pago for pago in self.pagos if pago.nombre_cliente == nombre_cliente]

    def get_by_id(self, pago_id):
        """Obtener un pago por su ID único."""
        return next((pago for pago in self.pagos if pago.id == pago_id), None)

    def delete(self, pago):
        """Eliminar un pago."""
        self.pagos.remove(pago)
