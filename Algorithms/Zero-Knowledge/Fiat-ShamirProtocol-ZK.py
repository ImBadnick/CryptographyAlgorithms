if __name__ == '__main__':
    print("Simulates the Fiat-Shamir protocol")
    p= int(input("Insert p: "))
    q= int(input("Insert q: "))
    s = int(input("Insert s: "))
    k = int(input("Insert k: "))
    n = p*q
    if (s>n):
        print("Error: s>(p*q)")
        exit(0)

    for i in range(k):
        print("\nProver")
        r = int(input("Insert r: "))
        u = (r**2) % n
        print("u is: " + str(u))
        print("\nVerifier")
        e = int(input("Insert e: "))
        print("\nProver")
        z = (r*(s**e)) % n
        print("z is: " + z)
        print("\nVerifier")
        x = (z**2) % n
        print("x is: " + x)
        if not (x == ((u*(t**e)) % n)): print("P not identified")

    print("P identified")