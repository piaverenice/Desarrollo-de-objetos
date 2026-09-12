# Crear dividir_seguro(a, b): si b es 0, mostrar error

def dividir_seguro(a, b):
    try:
        resultado = a / b
        print("Resultado", resultado)

    except ZeroDivisionError:
        print("No se puede dividir por cero")


dividir_seguro (10, 2)
dividir_seguro (10, 0)
