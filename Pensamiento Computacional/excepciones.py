import unittest

def busca_pais(pais):
    try:
        poblacion_paises = {
            "Argentina": 45000000,
            "Brasil": 200000000,
            "Colombia": 50000000,
        }
        return poblacion_paises[pais]
    except KeyError as e:
        return None

if __name__ == "__main__":
    pais = input("Escriba el nombre del pais el cual quiere ver la poblacion: ").lower().capitalize()
    if busca_pais(pais) == None:
        print("No se encuentra ese pais")
    else:
        print(busca_pais(pais))

class test_pais(unittest.TestCase):
        def test_pais(self):
            self.assertEqual(busca_pais(pais), 45000000)
unittest.main(verbosity=1)