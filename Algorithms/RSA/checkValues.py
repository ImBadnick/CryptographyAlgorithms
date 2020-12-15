import math

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount


def checkParams(p,q,e,d):
    n = p * q
    phi_n = phi(n)
    print("n = {}, phi_n = {}".format(n,phi_n))

    if(math.gcd(e,phi_n)!=1):
        print("MCD(e,phi_n) != 1 -> CONDITION NOT RESPECTED!")
    else:
        print("MCD(e,phi_n) == 1 -> CONDITION RESPECTED!")

    if(((e*d)%phi_n)!=1):
        print("(e*d mod phi_n) != 1 -> CONDITION NOT RESPECTED!")
    else:
        print("(e*d mod phi_n) == 1 -> CONDITION RESPECTED!")


if __name__ == '__main__':
    print("Checks if the values inserted for the RSA are ok")
    p = int(input("Insert p: "))
    q = int(input("Insert p: "))
    e = int(input("Insert e: "))
    d = int(input("Insert d: "))


    checkParams(p,q,e,d)


