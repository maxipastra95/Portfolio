class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pendiente(self, otra_coordenada):

        dist_y = self.y - otra_coordenada.y
        dist_x = self.x - otra_coordenada.x
        m = dist_y/dist_x

        return abs(m)

    def distancia(self, otra_coordenada):

        dist_x = (self.x - otra_coordenada.x)
        dist_y = (self.y - otra_coordenada.y)
        dist = (dist_x**2 - dist_y**2)**0.5

        return dist

if __name__ == "__main__":
    coor_1 = Coordenada(5, 10)
    coor_2 = Coordenada(-2, 7)
    print("La pendiente de la recta que pasa por ambos puntos es de:", round(coor_1.pendiente(coor_2), 2))
    print("La distancia entre los dos puntos es de: ", round(coor_1.distancia(coor_2), 2))