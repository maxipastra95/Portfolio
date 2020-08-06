def run():
    L = 1000
    c = 0
    p = 2**c
    while p < L:
        c += 1
        p = 2**c
        print(p)

if __name__ == "__main__":
    run()