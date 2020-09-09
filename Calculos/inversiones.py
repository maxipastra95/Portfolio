def analisis_inv(monto, tiempo, tasa):

    tasa = tasa/100
    acumulado = float(monto)

    for mes in range(tiempo):
        acumulado += monto + acumulado*tasa

    return acumulado



if __name__ == "__main__":

    monto = int(input("\nIngrese el monto en pesos a invertir mensualmente: "))
    tiempo = int(input("\nIngrese el tiempo en meses que piensa invertir: "))
    tasa = float(input("\nIngrese la tasa de interes estimada mensual en %: "))

    acumulado = analisis_inv(monto, tiempo, tasa)
    rendimiento = acumulado - monto*tiempo
    rendimiento_mensual = acumulado*(tasa/100)/130

    print(f"\nDespues de {tiempo} meses, y de haber ingresado ${monto} mensualmente: ")
    print(f"\n----> Su total acumulado sera de ${round(acumulado, 2)}")
    print(f"\n----> Su rendimiento total sera de ${round(rendimiento, 2)}")
    print(f"\n----> Su rendimiento total en dolares sera de U$D {round(rendimiento/130, 2)} ")
    print(f"\nA partir de este momento, puede sacar un rendimiento de U$D{round(rendimiento_mensual, 2)} mensual")