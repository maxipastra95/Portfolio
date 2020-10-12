class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')

if __name__ == '__main__':
    casilla = CasillaDeVotacion(147, ['La Plata', 'Ciudad de Santa Rosa', 'Posadas', 'San Salvador de Jujuy', 'La Rioja'])
    print(casilla.region)
    casilla.region = 'La Plata'
    print(casilla.region)
    casilla.region = 'San Salvador de Jujuy'
    print(casilla.region)
    casilla.region = 'Moron'
    print(casilla.region)