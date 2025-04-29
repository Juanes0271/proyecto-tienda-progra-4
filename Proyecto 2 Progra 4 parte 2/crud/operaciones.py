from model.clientes import Cliente
from model.facturas import Factura

def crear_cliente(clientes, nombre, cedula):
    cliente = Cliente(nombre, cedula)
    clientes.append(cliente)
    return cliente

def crear_factura(cliente):
    factura = Factura(cliente)
    cliente.agregar_factura(factura)
    return factura

def agregar_producto_a_factura(factura, producto):
    factura.agregar_producto(producto)

def buscar_por_cedula(clientes, cedula):
    for cliente in clientes:
        if cliente.cedula == cedula:
            print(f"\nCliente encontrado: {cliente.nombre}")
            if cliente.facturas:
                for factura in cliente.facturas:
                    print(f"\n Factura - Fecha: {factura.fecha.strftime('%Y-%m-%d')}")
                    for producto in factura.productos:
                        print(f" - Producto: {producto.nombre} | Precio: ${producto.precio:.2f}")
                    print(f"Total de Factura: ${factura.total:.2f}")
            else:
                print("No tiene facturas registradas.")
            return
    print(" Cliente no encontrado.")