from fractions import Fraction

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def calculateSum(x_p, y_p, x_q, y_q, module, a):
    pequalq = False
    if (y_p == 0 and x_p == 0):
        return x_q, y_q
    if (x_q == 0) and (y_q == 0):
        return x_p, y_p
    if (x_p == x_q and y_p == y_q): pequalq = True

    if module:
        module = int(module)
        if pequalq:
            lda = ((3 * (x_p ** 2) + a) * modinv(2 * y_p, module)) % module
        else:
            lda = ((y_q - y_p) * modinv(x_q - x_p, module)) % module

        x_s = ((lda ** 2) - x_p - x_q) % module
        y_s = ((-y_p) + lda * (x_p - x_s)) % module

    else:
        if pequalq:
            lda = ((3 * (x_p ** 2) + a) / (2*y_p))
        else:
            lda = ((y_q - y_p) * (x_q - x_p))

        x_s = ((lda ** 2) - x_p - x_q)
        y_s = ((-y_p) + lda * (x_p - x_s))



    print("Lambda = " + str(lda))
    print("xs = (" + str(Fraction(x_s)) + "," + str(Fraction(y_s)) + ") with point P = ({},{}) and Q = ({},{})".format(x_p, y_p, x_q, y_q))
    return x_s, y_s

if __name__ == '__main__':
    print("Does the sum of the points of the elliptic curve E_p(a,b)")
    x_p= int(input("Insert x_p: "))
    y_p= int(input("Insert y_p: "))
    x_q= int(input("Insert x_q: "))
    y_q = int(input("Insert y_q: "))
    a = int(input("Insert a: "))
    module = input("Insert module: ")

    calculateSum(x_p,y_p,x_q,y_q,module,a)
