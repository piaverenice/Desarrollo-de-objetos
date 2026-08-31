# Sistema simple de turnos
class Paciente:     
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f"Paciente: {self.nombre} - DNI: {self.dni}"

class Turno:
    def __init__(self, paciente, fecha, hora):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"{self.fecha} - {self.hora} - {self.paciente.dni}"

class Agenda:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        for t in self.turnos:
            if t.fecha == turno.fecha and t.hora == turno.hora:
                print("Ya existe un turno con esa fecha y hora.")
                return

        self.turnos.append(turno)
        print("Turno agendado correctamente")

    def listar_turnos(self):
        for turno in self. turnos:
            print(turno)



# Crear pacientes
paciente1 = Paciente("Leonel Mendoza", "41545678")
paciente2 = Paciente("Ludmila Solis", "42889980")
paciente3 = Paciente("Luz Salinas", "25565014")

# Crear turnos
turno1 = Turno(paciente1, "03/05/2026", "10:00")
turno2 = Turno(paciente2, "03/05/2026", "11:00")
turno3 = Turno(paciente3, "03/05/2026", "10:00")

# Crear agenda
agenda = Agenda()

# Agendar turnos
agenda.agregar_turno(turno1)
agenda.agregar_turno(turno2)
agenda.agregar_turno(turno3)

# Listar turnos
print("\nTurnos de la agenda:")
agenda.listar_turnos()
