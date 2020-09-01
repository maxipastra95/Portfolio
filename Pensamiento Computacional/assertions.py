import unittest

poblacion_paises = {
            "Argentina": 45000000,
            "Brasil": 200000000,
            "Colombia": 50000000,
        }

def agrega_pais(pais, habitantes):
    poblacion_paises[pais] = habitantes

if __name__ == "__main__":

    c = 0

    while c == 0:
        pais = input("Escriba el nombre del pais el cual quiere agregar: ").lower().capitalize()
        k = 0

        while k == 0:
            habitantes = input("Ingrese la cantidad de habitantes: ")
            try:
                int(habitantes)
                break
            except ValueError as e:
                print("No se puede amigo, pone numeritos, trata de nuevo \n")

        agrega_pais(pais, habitantes)
        c = int(input("Continuar?: "))

    for i, j in poblacion_paises.items():
        print(i, j)