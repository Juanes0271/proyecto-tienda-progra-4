from model.productos import ControlPlagas, ControlFertilizantes, Antibiotico
from crud.operaciones import crear_cliente, crear_factura, agregar_producto_a_factura, buscar_por_cedula

clientes = []

def menu():
    while True:
        print("\n Menú Principal ")
        print("1. Crear Cliente")
        print("2. Crear Factura")
        print("3. Buscar Cliente por Cédula")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            cedula = input("Cédula del cliente: ")
            crear_cliente(clientes, nombre, cedula)
            print("Cliente creado exitosamente.")

        elif opcion == "2":
            cedula = input("Ingrese la cédula del cliente: ")
            cliente = next((c for c in clientes if c.cedula == cedula), None)
            if cliente:
                factura = crear_factura(cliente)
                while True:
                    print("\nAgregar Producto:")
                    print("1. Control de Plagas")
                    print("2. Control de Fertilizantes")
                    print("3. Antibiótico")
                    print("4. Finalizar Factura")
                    seleccion = input("Seleccione una opción: ")

                    if seleccion == "1":
                        nombre = input("Nombre del producto: ")
                        precio = float(input("Precio: "))
                        registro = input("Registro ICA: ")
                        frecuencia = input("Frecuencia de aplicación: ")
                        carencia = input("Periodo de carencia: ")
                        producto = ControlPlagas(nombre, precio, registro, frecuencia, carencia)

                    elif seleccion == "2":
                        nombre = input("Nombre del producto: ")
                        precio = float(input("Precio: "))
                        registro = input("Registro ICA: ")
                        frecuencia = input("Frecuencia de aplicación: ")
                        ultima = input("Fecha de última aplicación: ")
                        producto = ControlFertilizantes(nombre, precio, registro, frecuencia, ultima)

                    elif seleccion == "3":
                        nombre = input("Nombre del antibiótico: ")
                        precio = float(input("Precio: "))
                        dosis = input("Dosis: ")
                        animal = input("Tipo de animal: ")
                        producto = Antibiotico(nombre, precio, dosis, animal)

                    elif seleccion == "4":
                        print("Factura finalizada.")
                        break
                    else:
                        print("Opción inválida.")
                        continue

                    agregar_producto_a_factura(factura, producto)
                    print(f"Producto {producto.nombre} agregado a la factura.")
            else:
                print("Cliente no encontrado.")

        elif opcion == "3":
            cedula = input("Ingrese la cédula del cliente a buscar: ")
            buscar_por_cedula(clientes, cedula)

        elif opcion == "4":
            print("Saliendo del sistema. ¡Gracias!")
            break

        else:
            print("Opción no válida.")