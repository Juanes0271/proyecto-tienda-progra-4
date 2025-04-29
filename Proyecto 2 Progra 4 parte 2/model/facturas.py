from datetime import datetime
class Factura:
    def __init__(self, cliente):
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos = []
        self.total = 0.0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio
