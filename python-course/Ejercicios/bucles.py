print("inicio del programa")
k = 1
def run(num, k):
    if num**k <= 1000:
        potencia = num ** k
        k += 1
        print(potencia)
        run(num, k)
    else:
        print("fin")
        
if __name__ == "__main__":
    num = int(input("Inserte un número: "))
    run(num, k)