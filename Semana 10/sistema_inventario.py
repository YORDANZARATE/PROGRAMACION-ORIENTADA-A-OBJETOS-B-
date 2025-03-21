import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario si existe."""
        if not os.path.exists(self.archivo):
            print(f"{self.archivo} no existe. Se creará uno nuevo.")
            return

        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    producto, cantidad = linea.strip().split(",")
                    self.productos[producto] = int(cantidad)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
        except PermissionError:
            print("No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda el inventario actual en el archivo."""
        try:
            with open(self.archivo, "w") as file:
                for producto, cantidad in self.productos.items():
                    file.write(f"{producto},{cantidad}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Ocurrió un error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad):
        """Añadir un producto al inventario."""
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_inventario()

    def actualizar_producto(self, nombre, cantidad):
        """Actualizar la cantidad de un producto."""
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            self.guardar_inventario()
        else:
            print(f"Producto {nombre} no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        """Eliminar un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
        else:
            print(f"Producto {nombre} no encontrado en el inventario.")

    def mostrar_inventario(self):
        """Mostrar los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto, cantidad in self.productos.items():
                print(f"{producto}: {cantidad}")

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            inventario.agregar_producto(nombre, cantidad)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_producto(nombre, cantidad)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    menu()

