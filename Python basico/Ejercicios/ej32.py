print("Bienvenido al sistema de ventas, para finalizar ingrese como monto de venta el valor 0.\n")
def run():
    monto = 0
    valor = 1
    while valor != 0:
        valor = int(input("Inserte el monto de la venta: $"))
        if valor < 0:
            print("Inserte un monto válido")
        else:
            monto += valor
    print(f"El monto total es de: ${monto}")

if __name__ == "__main__":
    run()