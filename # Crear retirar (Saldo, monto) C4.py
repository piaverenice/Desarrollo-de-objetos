# Crear retirar (saldo, monto): validar monto positivo y saldo suficiete

def retirar (saldo, monto):

    if monto <= 0:
        raise ValueError("El monto debe ser positivo")

    if monto > saldo:
        raise ValueError("Saldo insuficiente")

    return saldo - monto


try:
    saldo = retirar (20000, 5000)
    print("Retiro realizado")
    print("Saldo restante", saldo)

except ValueError as error:
    print("Error:", error)
    