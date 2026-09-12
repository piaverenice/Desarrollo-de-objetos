# Crear pedir_edad(): debe pedir una edad hasta que sea valida.

def pedir_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad > 0:
                return edad
            else:
                print("La edad debe ser positiva")
        except ValueError:
            print("Ingresa un numero valido")


edad = pedir_edad()
print("Edad ingresada:", edad)