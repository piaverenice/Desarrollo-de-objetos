# Crear una excepcion propia llamada ProductoSinStockError

class ProductoSinStockError (Exception):
    pass

def comprar(stock, cantidad):
    if cantidad > stock:
        raise ProductoSinStockError("No hay stock suficiente")

    return stock - cantidad


try:
    stock = comprar (10, 2)
    print("Compra realizada")
    print("Stock restante", stock)

except ProductoSinStockError as error:
    print("Error", error)