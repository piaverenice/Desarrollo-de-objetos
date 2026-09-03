# Crear clase cuenta con depositar, retirar y property saldo solo lectura
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto

    def retirar(self, monto):
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto


cuenta = Cuenta(100000)

print(cuenta.saldo)

cuenta.depositar(25000)
print(cuenta.saldo)

cuenta.retirar(30000)
print(cuenta.saldo)