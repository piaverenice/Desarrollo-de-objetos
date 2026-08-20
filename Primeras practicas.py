# Crear _int_ con nombre, precio y stock
# vender(): bajar stock solo si alcanza
# Reponer(): aumentar stock si cantidad >0
#crear dos productos y probarlos
class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad

    def reponer(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad

    def valor_inventario(self):
        return self.precio * self.stock


# Productos
p1 = Producto("Notebook", 500000, 10)
p2 = Producto("Mouse", 15000, 20)


# Pruebas
p1.vender(3)
p1.reponer(5)

p2.vender(5)
p2.reponer(10)

print(p1.nombre, p1.stock, p1.valor_inventario())
print(p2.nombre, p2.stock, p2.valor_inventario())