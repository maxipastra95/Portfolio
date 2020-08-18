# Diccionarios, comandos
def run():
    poblacion_paises = {
        "Argentina": 45000000,
        "Brasil": 200000000,
        "Colombia": 50000000,
    }
    print(poblacion_paises["Argentina"])
    print(poblacion_paises["Brasil"])

    for pais in poblacion_paises.keys():
        print(pais + "\n")
    
    for poblacion in poblacion_paises.values():
        print(str(poblacion) + "\n")
    
    for pais, poblacion in poblacion_paises.items():
        print(f"{pais} tiene {poblacion} habitantes")



if __name__ == "__main__":
    run()