
class Automovil:

    def __init__(self, modelo, marca, color, velocidad, cambio):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en_reposo"
        self._motor = None
        self.velocidad = velocidad
        self.cambio = cambio

    def acelerar(self, tipo='despacio'):
        if tipo = 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Caja_de_cambios:

    def __init__(self, primera, segunda, tercera, cuarta, quinta, reversa):
        self.primera = primera
        self.segunda = segunda
        self.tercera = tercera
        self.cuarta = cuarta
        self.quinta = quinta
        self.reversa = reversa

    def cambios(self, posicion):
        if velocidad < 10:
            self.cambio.primera
        elif velocidad > 10 and velocidad < 30:
            self.cambio.segunda
        elif velocidad > 30 and velocidad < 50:
            self.cambio.tercera
    

