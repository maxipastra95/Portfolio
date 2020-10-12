import math

class Contable:

    def __init__(self, precio, cantidad):
        self.precio = precio
        self.cantidad = cantidad

    def monto(self):
        return self.precio*self.cantidad
    
class Comida(Contable):

    def __init__(self, precio, cantidad):
        super().__init__(precio, cantidad)

class Bebida(Contable):

    def __init__(self, precio, vasos):
        super().__init__(precio, vasos)

if __name__ == '__main__':

    comida = Comida(150,2)
    bebida = Bebida(80, 2)
    
    print(f'El precio total es de ${comida.monto()+bebida.monto()}')