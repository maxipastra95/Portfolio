frase = input("Ingrese un texto: ")
c = len(frase)
frase_invertida = ""
for letra in range(len(frase)):
    frase_invertida = frase_invertida + frase[c-1]
    c -= 1
print(frase_invertida)