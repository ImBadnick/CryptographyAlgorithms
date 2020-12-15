if __name__ == '__main__':
    print("Checks if the E_p(a,b) is an abelian group")
    a = int(input("Insert a: "))
    b = int(input("Insert b: "))
    module = input("Insert module: ")

    if module:
        module = int(module)
        if (((4 * (a ** 3) + 27 * (b ** 2)) % module) != 0):
            print("True")
        else:
            print("False")

    else:
        if((4 * (a ** 3) + 27 * (b ** 2)) != 0):
            print("True")
        else:
            print("False")