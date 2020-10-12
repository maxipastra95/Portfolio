
class Bicicleta():

    def __init__(self):
        pass

    def andar(self, velocidad, pozos):
        self._pedalear(velocidad)
        self._frenar(velocidad)
        self._agarre(velocidad)
        self._sentado(pozos)

    def _pedalear(self, velocidad):
        if velocidad == 'rapido':
            print(f'Pedaleo {velocidad} y fuerte')
        else:
            print(f'Pedaleo {velocidad} y despacio')

    def _frenar(self, velocidad):
        if velocidad == 'rapido':
            print('Freno de golpe')
        else:
            print('Todavía no es hora de frenar')

    def _agarre(self, velocidad):
        if velocidad == 'rapido':
            print('Me sostengo firmemente')
        else:
            print('Voy relajado sobre el manubrio')

    def _sentado(self, pozos):
        if pozos == True:
            print('Me levanto del asiento')
        else:
            print('Voy sentado y relajado')

if __name__ == '__main__':
    bici = Bicicleta()
    bici.andar('rapido', True)