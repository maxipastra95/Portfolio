ti = 1.04
ii = float(input("Ingrese inversión inicial: "))
b1 = ii*ti
b2 = ii*ti*ti
b3 = ii*ti*ti*ti
print(f"El balance después del primer año es: {round(b1, 2)}")
print(f"El balance después del segundo año es: {round(b2, 2)}")
print(f"El balance después del tercer año es: {round(b3, 2)}")