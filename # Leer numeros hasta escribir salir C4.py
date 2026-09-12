# Leer numeros hasta escribir salir y manejar valores invalidos

while True:

    dato = input("Ingresar un numero o escribir 'salir': ")

    if dato == "salir":
        print("Programa finalizado")
        break

    try:
        numero = int(dato)
        print("Numero ingresado", numero)

    except ValueError:
        print("Valor invalido. Debes ingresar un numero")