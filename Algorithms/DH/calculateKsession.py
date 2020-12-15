if __name__ == '__main__':
    print("Calculates k[session] of DH cipher")
    try:
        g = int(input("Insert g: "))
        p = int(input("Insert p: "))
        x = int(input("Insert x: "))
        y = int(input("Insert y: "))
    except ValueError:
        print("Input is not an integer!")
        exit(0)

    Ksession = (g**(x*y)) % p
    print(Ksession)
