# def analizador(numero):
#     respuesta = 0.0
#     epsilon = 0.0001
#     while respuesta**2 <= numero:
#         respuesta += epsilon
#         if (respuesta+epsilon)**2 >= numero:
#             break
#     return(respuesta)


# if __name__ == "__main__":
#     numero = int(input("Inserte un número positivo para hallar la raíz: "))
#     print("La raíz es aproximadamente:", analizador(numero))

def analizador(numero):
    epsilon = 0.0001
    respuesta = numero / 2
    bajo = 0
    while abs(respuesta**2 - numero) >= epsilon:
        print(respuesta)
        if respuesta**2 - numero > 0:
            alto = respuesta
        else:
            bajo = respuesta
        respuesta = (alto + bajo)/2

    else:
        return(respuesta)


if __name__ == "__main__":
    numero = int(input("Inserte un numero positivo para hallar la raiz: "))
    print("La raiz de su numero es: ", analizador(numero))