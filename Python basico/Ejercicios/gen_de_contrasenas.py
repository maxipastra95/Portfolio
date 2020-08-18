# import random

# def generador():
#     mayus = ["A","B","C","D","E","F","G"]
#     minus = ["a","b","c","d","e","f","g" ]
#     simb = ["!","#","$","&","/","(",")"]
#     num = ["0","1","2","3","4","5","6","7","8","9"]

#     caracteres = mayus + minus + simb + num
    
#     contrasena = []

#     for i in range(15):
#         caracter_random = random.choice(caracteres)
#         contrasena.append(caracter_random)

#     contrasena = ''.join(contrasena)
#     return contrasena

# def run():
#     contrasena = generador()
#     print(f"Tu nueva contraseña es {contrasena}")

# if __name__ == "__main__":
#     run()

import random

def generador():

    contrasena = []

    for i in range(15):

        caracter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!$%&/@")
        contrasena.append(caracter)
        
    contrasena = ''.join(contrasena)
    return contrasena

def run():
    contrasena = generador()
    print(f"Tu nueva contraseña es: {contrasena}")

if __name__ == "__main__":
    run()
