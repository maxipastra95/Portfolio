demo_list = [1,"hello",1.34,True,[1,2,3]]
colors = ["red","green","blue"]

numbers_list = list((1,2,3,4))
# print(type(numbers_list))

# r = list(range(1,1000)) ---> Agrega un rango de números a una lista
# print(r)

# print(colors[1]) ---> Muestra el dato en la posición deseada

print("violet" in colors) # ---> Se fija si está ese elemento en la lista y lo muestra

# colors[1] = "skyblue" ---> Reemplaza el dato en la posición deseada

colors.append("violet") # ---> Añade un elemento a la lista

colors.extend(["violet", "yellow"]) # ---> Añade varios elementos a una lista desde otra lista

colors.insert(1, "violet") # ---> Añade otro elemento en la posición deseada sin reemplazar
colors.insert(len(colors), "violet") # ---> Añade un elemento en la última posición de la lista

colors.pop() # ---> Elimina el último elemento de la lista
colors.pop(1) # ---> Elimina el elemento deseado de la lista desde su posición

colors.remove("green") # ---> Elimina el elemento deseado desde su nombre

colors.clear # ---> Elimina todos los elementos

colors = ["red","green","blue"]

colors.sort(reverse=True) # ---> Ordena los elementos y los da vuelta con "reverse"

print(colors.index("red")) # ---> Muestra la posición del elemento red 

colors = ["red","green","blue", "red"]

print(colors.count("red")) # ---> Cuenta la cantidad de "red" que hay y los muestra