def conejos(m):
    # Halla la cantidad de conejos de una población de un macho y una hembra después de "m" meses
    if m == 1 or m == 0:
        return 1
    cantidad_de_conejos = conejos(m-1) + conejos(m-2)
    return cantidad_de_conejos


if __name__ == "__main__":
    k = 0
    while k == 0:

        import time
        m = int(input("Cuantos meses pasaron?: "))
        t = time.time()*1000
        print(f"Hay {conejos(m)} en total después de {m} meses")
        print("Tiempo de procesamiento: \n", round((time.time()*1000)-t, 4), "ms")
        k = int(input("Desea seguir calculando?: "))
        