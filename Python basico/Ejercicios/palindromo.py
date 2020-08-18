# Detector de palíndromos

# palabra = input("Inserte una palabra o frase: ").lower().replace(" ","")

# if palabra == palabra[::-1]:
#     print("Es palíndromo")
#     print(palabra)
# else:
#     print("No es palíndromo")

texto = "Hola como estás"
print(texto[::-1].replace(" ","").lower())