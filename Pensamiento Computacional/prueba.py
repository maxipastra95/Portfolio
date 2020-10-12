# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, "No se permiten str vacios"

        primeras_letras.append(palabra[0])
        
        return primera_letra

lista = ["hola", "como", "estas"]
lista.append(input("Inserte palabras: "))
print (primera_letra(lista))