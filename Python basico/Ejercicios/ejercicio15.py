menu = """Bienvenidos al conversor de monedas
para comenzar digite un número:
1 - ARS a USD
2 - COP a USD
3 - CLP a USD
----> """
opcion = input(menu)
def conv(usd):
    valor = float(input("Inserte el monto en pesos: "))
    conv = round(usd/valor, 2)
    print(f"El valor de ${valor} en dólares es de {usd}")

if opcion == "1":
    conv(72.56)
elif opcion == "2":
    conv(3775.5)
elif opcion == "3":
    conv(777.4)
else: 
    print("Ingrese una opcion correcta")