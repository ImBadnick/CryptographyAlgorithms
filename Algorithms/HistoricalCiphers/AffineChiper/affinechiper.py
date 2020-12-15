import math

if __name__ == '__main__':
    print("Calculates the cripto from the message")
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    try:
        msg = input("Insert msg: ")
        a = int(input("Insert a: "))
        b = int(input("Insert b: "))
    except ValueError:
        print("Value not an integer")
        exit(0)

    if (math.gcd(a,26)) == 1:
        cripto = ''.join([alphabet[(alphabet.index(c) + ((a*alphabet.index(c)+b) % len(alphabet))) % len(alphabet)]
                   if c in alphabet else c for c in msg])
    else:
        print("mcd(a,26)!=1")

    print("Cripto is: " + cripto)
