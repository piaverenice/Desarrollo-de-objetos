from django.core.management.base import BaseCommand
from biblioteca.models import Libro, Socio, Reserva
from django.db.models import Q
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = "Sistema de reservas de libros de una biblioteca"

    def mostrar_libro(self, libro):
        print(
            f"ISBN: {libro.isbn} | "
            f"Titulo: {libro.titulo} | "
            f"Autor: {libro.autor} | "
            f"Disponibles: "
            f"{libro.cantidad_disponible}/{libro.cantidad_total}"
        )

    def mostrar_reserva(self,reserva):
        print(
            f"ID: {reserva.id} | "
            f"Socio: {reserva.socio.numero_socio} - "
            f"{reserva.socio.nombre} {reserva.socio.apellido} | "
            f"Libro: {reserva.libro.titulo} | "
            f"Fecha: {reserva.fecha_reserva:%d/%m/%Y %H:%M} | "
            f"Estado: {reserva.estado}"
        )

    def handle(self, *args, **options):
        while True:
            print("\n=== SISTEMA DE BIBLIOTECA ===")
            print("1. Registrar libro")
            print("2. Registrar socio")
            print("3. Listar libros")
            print("4. Buscar libro")
            print("5. Listar socios")
            print("6. Realizar reserva")
            print("7. Cancelar reserva")
            print("8. Retirar libro reservado")
            print("9. Devolver libro")
            print("10. Listar reservas de un socio")
            print("11. Listar todas las reservas")
            print("12. Consultas")
            print("0. Salir")

            opcion = input("Elegi una opcion: ")


            if opcion == "1":
                isbn = input("Ingresa el ISBN: ").strip()

                if not isbn:
                    print("El ISBN no puede estar vacio.")
                    continue

                if Libro.objects.filter(isbn=isbn).exists():
                    print("Ya existe un libro con ese ISBN.")
                    continue

                titulo = input("Ingresa el titulo: ").strip()
                autor = input("Ingresa el autor: ").strip()

                if not titulo or not autor:
                    print("El titulo y el autor son obligatorios.")
                    continue

                try:
                    anio = int(input("Año de publicación: "))
                    cantidad = int(input("Cantidad total de ejemplares: "))

                    if anio <= 0 or cantidad <= 0:
                        print("El año y la cantidad deben ser mayores que cero.")
                        continue

                    libro = Libro(
                        isbn=isbn,
                        titulo=titulo,
                        autor=autor,
                        anio_publicacion=anio,
                        cantidad_total=cantidad,
                        cantidad_disponible=cantidad
                    )

                    libro.full_clean()
                    libro.save()

                    print("¡Libro registrado correctamente!")

                except ValueError:
                    print("Error: ingresa numeros validos para el año y la cantidad.")

                except ValidationError as error:
                    for campo, mensjes in error.message_dict.items():
                        print(f"{campo}: {'; '.join(mensjes)}")

            elif opcion == "2":
                try:
                    numero_socio = int(input("Numero de socio: "))

                    if numero_socio <= 0:
                        print("El numero de socio debe ser mayor que cero.")
                        continue

                    if Socio.objects.filter(
                        numero_socio=numero_socio
                    ).exists():
                        print("Ese numero de socio ya esta registrado.")
                        continue
                    nombre = input("Nombre: ").strip()
                    apellido = input("Apellido: ").strip()
                    dni = input("DNI: ").strip()
                    email = input("Email: ").strip()

                    if not nombre or not apellido or not dni or not email:
                        print("Todos los campos son obligatorios.")
                        continue
                    if Socio.objects.filter(dni=dni).exists():
                        print("Ese DNI ya esta registrado.")
                        continue

                    socio = Socio(
                        numero_socio=numero_socio,
                        nombre=nombre,
                        apellido=apellido,
                        dni=dni,
                        email=email,
                        activo=True
                    )

                    socio.full_clean()
                    socio.save()

                    print("¡Socio registrado correctamente!")

                except ValueError:
                    print("El numero de socio debe ser un numero entero.")

                except ValidationError as error:
                    for campo, mensjes in error.message_dict.items():
                        print(f"{campo}: {'; '.join(mensjes)}")

            elif opcion == "3":
                libros = Libro.objects.all()

                if libros.exists():
                    for libro in libros:
                        self.mostrar_libro(libro)
                else:
                    print("No hay libros registrados.")


            elif opcion == "4":
                busqueda = input(
                    "Ingresa ISBN, titulo o autor: "
                ).strip()

                if not busqueda:
                    print("Debes ingresar un dato para buscar.")
                    continue

                libros = Libro.objects.filter(
                    Q(isbn__icontains=busqueda)
                    | Q(titulo__icontains=busqueda)
                    | Q(autor__icontains=busqueda)
                )

                if libros.exists():
                    for libro in libros:
                        self.mostrar_libro(libro)
                else:
                    print("No se encontraron libros.")

            
            elif opcion == "5":
                socios = Socio.objects.all()

                if socios.exists():
                    for socio in socios:
                        print(
                            f"N.° socio: {socio.numero_socio} | "
                            f"Nombre: {socio.nombre} {socio.apellido} | "
                            f"DNI: {socio.dni} | "
                            f"Email: {socio.email} | "
                            f"Estado: {'Activo' if socio.activo else 'Inactivo'}"
                        )
                else:
                    print("No hay socios registrados.")

            elif opcion == "6":
                    try:
                        numero_socio = int(input("Numero de socio: "))
                        isbn = input("ISBN del libro: ").strip()

                        socio = Socio.objects.get(
                            numero_socio=numero_socio
                        )
                        libro = Libro.objects.get(isbn=isbn)

                        reserva = Reserva(
                            socio=socio,
                            libro=libro
                        )

                        if reserva.confirmar_reserva():
                            print("¡Reserva realizada correctamente!")
                        else:
                            print(
                                "No se pudo realizar la reserva. "
                                "Verifica que el socio este activo, "
                                "haya ejemplares disponibles y no tenga "
                                "otra reserva activa de ese libro."
                            )

                    except ValueError:
                        print("El numero de socio debe ser un numero entero.")

                    except Socio.DoesNotExist: 
                        print("No existe un socio con ese numero.")

                    except Libro.DoesNotExist:
                        print("No existe un libro con ese ISBN.")

            elif opcion == "7":
                try:
                    id_reserva = int(input("ID de la reserva a cancelar: "))

                    reserva = Reserva.objects.get(id=id_reserva)

                    if reserva.cancelar_reserva():
                        print("¡Reserva cancelada correctamente!")
                    else:
                        print(
                            "No se pudo cancelar la reserva. "
                            "Verifica que exista y que este pendiente."
                        )

                except ValueError:
                    print("El ID de la reserva debe ser un numero entero.")

                except Reserva.DoesNotExist:
                    print("No existe una reserva con ese ID.")

            elif opcion == "8":
                try: 
                    id_reserva = int(input("ID de la reserva a retirar: "))

                    reserva = Reserva.objects.get(id=id_reserva)

                    if reserva.retirar_reserva():
                        print("¡Retiro registrado correctamente!")
                    else:
                        print(
                            "No se pudo registrar el retiro. "
                            f"La reserva esta en estado {reserva.estado}. "
                            "Solo se pueden retirar reservas pendientes."
                        )

                except ValueError:
                    print("El ID de la reserva debe ser un numero entero.")

                except Reserva.DoesNotExist:
                    print("No existe una reserva con ese ID.")
            
            elif opcion == "9":
                try:
                    id_reserva = int(input("ID de la reserva a finalizar: "))

                    reserva = Reserva.objects.get(id=id_reserva)

                    if reserva.finalizar_reserva():
                        print("¡Devolucion registrada correctamente!")
                    else:
                        print(
                            "No se pudo registrar la devolucion. "
                            "La reserva debe estar RETIRADA y el stock "
                            "debe permitir devolver el ejemplar. "
                            f"Estado actual: {reserva.estado}."
                        )

                except ValueError:
                    print("El ID de la reserva debe ser un numero entero.")

                except Reserva.DoesNotExist:
                    print("No existe una reserva con ese ID.")

            elif opcion == "10":
                try:
                    numero_socio = int(input("Numero de socio: "))

                    socio = Socio.objects.get(
                        numero_socio=numero_socio
                    )

                    reservas = (
                        Reserva.objects.filter(socio=socio)
                        .select_related("socio", "libro")
                        .order_by("fecha_reserva", "id")
                    )

                    if reservas.exists():
                        print(
                            f"\nReservas de {socio.nombre} "
                            f"{socio.apellido}:"
                        )

                        for reserva in reservas:
                            self.mostrar_reserva(reserva)
                    else:
                        print("El socio no tiene reservas registradas.")

                except ValueError:
                    print("El numero de socio debe ser un numero entero.")

                except Socio.DoesNotExist:
                    print("No existe un socio con ese numero.")

            elif opcion == "11":
                reservas = (
                    Reserva.objects.select_related("socio", "libro")
                    .order_by("fecha_reserva", "id")
                )

                if reservas.exists():
                    for reserva in reservas:
                        self.mostrar_reserva(reserva)
                else:
                    print("No hay reservas registradas.")

            elif opcion == "12":
                print("\n=== CONSULTAS ===")
                print("1. Libros disponibles")
                print("2. Libros sin disponibilidad")
                print("3. Reservas pendientes")
                print("4. Reservas de un libro")
                print("5. Socios activos")

                consulta = input("Elegi una consulta: ").strip()

                if consulta in ["1", "2"]:
                    if consulta == "1":
                        libros = Libro.objects.filter(
                            cantidad_disponible__gt=0
                        )
                    else:
                        libros = Libro.objects.filter(
                            cantidad_disponible=0
                        )

                    if libros.exists():
                        for libro in libros:
                            self.mostrar_libro(libro)
                    else:
                        print("No hay libros que cumplan con esa condicion.")

                elif consulta in ["3", "4"]:
                    if consulta == "3":
                        reservas = Reserva.objects.filter(
                            estado="PENDIENTE"
                        )
                    else:
                        isbn = input("ISBN del libro: ").strip()

                        try:
                            libro = Libro.objects.get(isbn=isbn)
                        except Libro.DoesNotExist:
                            print("No existe un libro con ese ISBN.")
                            continue

                        reservas = Reserva.objects.filter(libro=libro)

                    reservas = reservas.select_related(
                        "socio", "libro"
                    ).order_by("fecha_reserva", "id")

                    if reservas.exists():
                        for reserva in reservas:
                            self.mostrar_reserva(reserva)
                    else:
                        print("No hay reservas que cumplan esa condicion.")

                elif consulta == "5":
                    socios = Socio.objects.filter(activo=True)

                    if socios.exists():
                        for socio in socios:
                            print(
                                f"Numero: {socio.numero_socio} | "
                                f"Nombre: {socio.nombre} "
                                f"{socio.apellido}"
                            )
                    else:
                        print("No hay socios activos.")

                else:
                    print("Consulta invalida.")


            elif opcion == "0":
                print("¡Hasta luego!")
                break

            else: 
                print("Opcion invalida.")
