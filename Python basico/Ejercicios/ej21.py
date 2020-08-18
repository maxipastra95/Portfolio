def run():
    k = 1
    while k == 1:
        usuario = input("Inserte nombre de usuario: ")
        contraseña = input("Inserte la contraseña: ")
        if usuario != "Gwenevere" or contraseña != "excalibur" :
            print("El usuario o la contraseña son incorrectos, intente nuevamente \n")
        else:
            k = 0




if __name__ == "__main__":
    run()
    print("Acceso concedido")