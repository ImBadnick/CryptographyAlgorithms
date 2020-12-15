if __name__ == '__main__':
    print("Calculates X = (g^x) mod p")
    try:
        y = int(input("Insert g: "))
        z = int(input("Insert p: "))
        s = int(input("Insert x: "))
    except ValueError:
        print("Input is not an integer!")
        exit(0)

    X = (g**x) % p
    print(X)