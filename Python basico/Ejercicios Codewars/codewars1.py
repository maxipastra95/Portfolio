import unittest

def reverse(word):
    return word[::-1]

class reverseTest(unittest.TestCase):

    def test_reverse(self):
        resultado = reverse('world')

        self.assertEqual(resultado, "dlrow")


if __name__ == "__main__":
    unittest.main()