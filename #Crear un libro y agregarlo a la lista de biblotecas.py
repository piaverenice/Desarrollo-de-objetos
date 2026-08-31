#Crear un libro y agregarlo a la lista de biblotecas
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)


# Crear una biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Crear un libro
libro1 = Libro("El Principito", "Antoine de Saint-Exupery")

# Agregar el libro a la biblioteca
biblioteca.agregar_libro(libro1)

# Mostrar los libros de la biblioteca
print(biblioteca.libros)

