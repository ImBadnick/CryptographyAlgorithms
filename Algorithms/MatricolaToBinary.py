if __name__ == '__main__':
    print("Transforms the matricola digit to binary and the whole number to binary")
    try:
        m = int(input("Insert matricola: "))
    except ValueError:
        print("Input is not an integer!")
        exit(0)

    res = [int(x) for x in str(m)]

    for i in res:
        print("The number " + str(i) + " in binary is: {0:b}".format(i))

    print("\n\n\nThe number " + str(m) + " in binary is: {0:b}".format(m))