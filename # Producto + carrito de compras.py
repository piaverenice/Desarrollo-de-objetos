# Producto + carrito de compras 
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class CarritoCompra:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        if producto.precio > 0:
            self.productos.append(producto)
        else:
            print("No se puede agregar un producto con precio menor o igual a 0")

    def total(self):
        total = 0

        for producto in self.productos:
            total += producto.precio

        return total

    def mostrar(self):
        for producto in self.productos:
            print(producto)


producto1 = Producto("Notebook", 500000)
producto2 = Producto("Mouse", 15000)
producto3 = Producto("Teclado", 30000)

carrito = CarritoCompra()

carrito.agregar(producto1)
carrito.agregar(producto2)
carrito.agregar(producto3)

carrito.mostrar()

print("Total a pagar:", carrito.total())