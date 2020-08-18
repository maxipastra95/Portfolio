def run():
    c = 0
    for año in range(2020,2120):
        if año % 4 == 0 and año % 100 != 0:
            print(f"El año {año} bisiesto")
            c += 1
        else:
            pass
    print(f"Hay {c} años bisiestos")

if __name__ == "__main__":
    run()