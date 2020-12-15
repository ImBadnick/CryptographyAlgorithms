import sympy
import math
import random

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m): #Calculates x = a^(-1) mod m
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m



if __name__ == '__main__':
    print("Calculates the critto and decripto of RSA cipher")
    m = input("Insert msg: ")
    try:
        p = int(input("Insert p: "))
        q = int(input("Insert q: "))
        e = input("Insert e: ")
    except ValueError:
        print("Values are not integers")
        exit(0)


    if(not(sympy.isprime(p)) or not(sympy.isprime(q))):
        print("p or q are not prime values")
        exit(0)

    n = p*q
    phi_n = (p-1)*(q-1)

    blockDimension = (math.frexp(n)[1] - 1)
    print("Cripto block dimension = InferiorPart(log_2(n)) = " + str(blockDimension))

    mList = [m[i: i + blockDimension] for i in range(0, len(m), blockDimension)]
    print("MSG BLOCKS: " + mList)
    try:
        m = [int(i,2) for i in mList]
    except ValueError:
        m = [int(i) for i in mList]


    if e: e = int(e)
    else :
        while True:
            e = random.randint(1,phi_n)
            if(math.gcd(e,phi_n)==1): break

    print("e value is: " + str(e))

    d = modinv(e,phi_n)

    print("d value is: " + str(d))

    criptoList = []
    k = 0
    for m_i in m:
        cripto = (m_i ** e) % n
        criptoList.append(cripto)
        print("Cripto_"+ str(k) + " is: " + str(cripto))
        k+=1

    k = 0
    for c_i in criptoList:
        decripto = (c_i ** e) % n
        print("Decripto_"+ str(k) +" is: " + str(cripto))
        k+=1




