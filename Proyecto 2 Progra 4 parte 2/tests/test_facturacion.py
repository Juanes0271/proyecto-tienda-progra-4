import unittest
from model.clientes import Cliente
from model.productos import ControlPlagas
from model.facturas import Factura

class TestFacturacion(unittest.TestCase):
    def test_relacion_cliente_factura(self):
        cliente = Cliente("Pedro", "112233")
        factura = Factura(cliente)
        producto = ControlPlagas("Insecticida", 80000, "ICA-123", "30 días", "15 días")
        factura.agregar_producto(producto)
        cliente.agregar_factura(factura)

        self.assertEqual(cliente.facturas[0].productos[0].nombre, "Insecticida")
        self.assertEqual(cliente.facturas[0].total, 80000)

if __name__ == "__main__":
    unittest.main()