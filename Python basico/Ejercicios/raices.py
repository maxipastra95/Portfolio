def analizador1(numero):
    import time
    respuesta = 0.0
    epsilon = 0.0001
    t = float(time.time())
    while respuesta**2 <= numero:
        respuesta += epsilon
        if (respuesta+epsilon)**2 >= numero:
            break
    print("Tiempo de procesamiento: ", round(time.time()-t, 10), "segundos")
    return(respuesta)

def analizador2(numero):
    import time
    epsilon = 0.0001
    respuesta = numero / 2
    bajo = 0
    t = time.time()
    while abs(respuesta**2 - numero) >= epsilon:
        if respuesta**2 - numero > 0:
            alto = respuesta
        else:
            bajo = respuesta
        respuesta = (alto + bajo)/2
    print("Tiempo de procesamiento: ", round(time.time()-t, 10) , "segundos")
    return(respuesta)


if __name__ == "__main__":
    numero = int(input("Inserte un numero positivo para hallar la raiz: "))
    menu = """Que metodo prefiere usar?
    Inserte " 1 " para usar el método ineficiente
    Inserte " 2 " para usar el método eficiente

    ---> """

    k = int(input(menu))
    if k == 1:
        print("La raiz del numero es:", analizador1(numero))
    elif k == 2:
        print("La raiz del numero es:", analizador2(numero))
    else:
        print("Numero incorrecto")