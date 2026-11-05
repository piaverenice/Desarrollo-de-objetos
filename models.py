from django.db import models
from django.db import transaction

class Libro(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.PositiveIntegerField()
    cantidad_total = models.PositiveIntegerField()
    cantidad_disponible = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(cantidad_disponible__gte=0)
                    & models.Q(
                        cantidad_disponible__lte=models.F("cantidad_total")
                    )
                ),
                name="libro_stock_dentro_de_limites",
            )
        ]

    def __str__(self):
        return self.titulo

    def esta_disponible(self):
        return self.cantidad_disponible > 0

    def reservar_ejemplar(self):
        if self.esta_disponible():
            self.cantidad_disponible -= 1
            self.save()
            return True
        return False

    def liberar_ejemplar(self):
        if self.cantidad_disponible < self.cantidad_total:
            self.cantidad_disponible += 1
            self.save()
            return True
        return False

class Socio(models.Model):
    numero_socio = models.PositiveBigIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        if self.activo:
            return f"{self.nombre} {self.apellido} - Activo"
        else:
            return f"{self.nombre} {self.apellido} - Inactivo"

    def esta_activo(self):
        return self.activo
    
class Reserva(models.Model):
    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("RETIRADA", "Retirada"),
        ("CANCELADA", "Cancelada"),
        ("FINALIZADA", "Finalizada"),
    ]

    socio = models.ForeignKey(Socio, on_delete=models.PROTECT)
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default="PENDIENTE"
    )

    def __str__(self):
        return f"Reserva de {self.socio} - {self.libro}"

    def puede_reservar(self):
        return self.socio.esta_activo() and self.libro.esta_disponible()

    @transaction.atomic
    def confirmar_reserva(self):
        if self.pk is not None or self.estado != "PENDIENTE":
            return False

        if not self.puede_reservar():
            return False

        reserva_existente = Reserva.objects.filter(
            socio=self.socio,
            libro=self.libro,
            estado__in=["PENDIENTE", "RETIRADA"]
        ).exists()

        if reserva_existente:
            return False

        if self.libro.reservar_ejemplar():
            self.save()
            return True
        
        return False

    @transaction.atomic
    def cancelar_reserva(self):
        if self.pk is None or self.estado != "PENDIENTE":
            return False

        if not self.libro.liberar_ejemplar():
            return False

        self.estado = "CANCELADA"
        self.save()
        return True

    def retirar_reserva(self):
        if self.pk is None or self.estado != "PENDIENTE":
            return False
        self.estado = "RETIRADA"
        self.save()
        return True
    
    @transaction.atomic
    def finalizar_reserva(self):
        if self.pk is None or self.estado != "RETIRADA":
            return False

        if not self.libro.liberar_ejemplar():
            return False

        self.estado = "FINALIZADA"
        self.save()
        return True