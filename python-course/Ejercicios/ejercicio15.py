menu = """Bienvenidos al conversor de monedas
para comenzar digite un número:
1 - ARS a USD
2 - COP a USD
3 - CLP a USD
----> """
opcion = input(menu)
def conv():
    valor = float(input("Inserte el monto en pesos: "))
    conv = round(usd/valor, 2)
    print(f"El valor de ${valor} en dólares es de {usd}")

if opcion == "1":
    usd = 72.56
    conv()
elif opcion == "2":
    usd = 3775.5
    conv()
elif opcion == "3":
    usd = 777.4
    conv()
else: 
    print("Ingrese una opcion correcta")