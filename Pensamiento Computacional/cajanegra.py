import unittest

def suma(num1,num2):
    return abs(num1) + num2

class CajaNegraTest(unittest.TestCase):

    def test_sumapositivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_sumanegativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

if __name__ == "__main__":
    unittest.main()