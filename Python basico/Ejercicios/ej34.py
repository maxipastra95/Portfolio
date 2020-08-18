def run():
    opcion = input("Desea analizar las calificaciones de los alumnos? Presione 'S' para analizar: ")
    caltot = 0
    aprobados = 0
    alumnos = 0
    while opcion == "S":
        cal = int(input("Inserte la calificación del alumno: "))
        caltot += cal
        if cal > 4:
            aprobados += 1
        alumnos += 1
        opcion = input("Desea seguir analizando? Presione 'S': ")
    print(f"El % de aprobados es de {round((aprobados/alumnos)*100,2)} %")
    print(f"El puntaje promedio de los aprobados es de {round(caltot/aprobados,2)}")
if __name__ == "__main__":
    run()