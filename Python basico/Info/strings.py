myStr = "Hello World z"

# print(dir(myStr)) 

# Distintas maneras de modificar el texto de la variable que ya tengo

print(myStr.upper()) # Todo mayúscula
print(myStr.lower()) # Todo minúscula
print(myStr.swapcase()) # Invierte las mayúsculas
print(myStr.capitalize()) # La primera es mayúscula
print(myStr.replace('Hello','bye').upper()) # Reemplaza el caracter
print(myStr.strip()) # Elimina los espacios
print(myStr.count(' ')) # Cuenta la cantidad de caracteres que hay
print(myStr.startswith('Hello')) # Se fija si empieza con ese caracter
print(myStr.endswith("World")) # Se fija si termina con ese caracter

print(myStr.split("o")) # Lo separa en listas
print(myStr.find("z")) # Busca la posicion del caracter

print(len(myStr)) # Longitud del string
print(myStr.index('e')) # se fija donde esta

print(myStr.isnumeric()) # se fija si es un número
print(myStr.isalpha()) # se fija si es alfanumérico

print(myStr[0])
print(myStr[-1])

print("My name is" + myStr)
print(f"My name is {myStr}")
