# Detector de palíndromos

palabra = input("Inserte una palabra o frase: ").lower().replace(" ","")

if palabra == palabra[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")