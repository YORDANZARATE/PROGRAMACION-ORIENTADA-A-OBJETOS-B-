import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()

    def buscar_producto(self, nombre):
        return [prod for prod in self.productos.values() if nombre.lower() in prod.nombre.lower()]

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as archivo:
            json.dump({id: vars(prod) for id, prod in self.productos.items()}, archivo)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                self.productos = {id: Producto(**prod) for id, prod in datos.items()}
        except FileNotFoundError:
            self.productos = {}


def menu():
    inventario = Inventario()
    while True:
        print("\n1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja vacío para no cambiar): ")
            precio = input("Nuevo precio (deja vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            for producto in resultados:
                print(producto)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
