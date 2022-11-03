"""Clase de la tarjeta"""
class Tarjeta:
    def __init__(self, num, pin):
        self.Numero = num
        self.Pin = pin
        self.Saldo = 0
    def __str__(self):
        return f"""
# Cuenta: {self.Numero}
Pin: -----
Saldo: {self.Saldo}"""