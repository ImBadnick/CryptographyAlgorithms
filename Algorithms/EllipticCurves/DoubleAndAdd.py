def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def modinv(a, m): #Calculates the modular inverse
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def calculateSum(x_p,y_p,x_q,y_q,module,a):
    pequalq = False
    if(y_p == 0 and x_p == 0):
        return x_q,y_q
    if(x_q == 0) and (y_q==0):
        return x_p,y_p
    if(x_p == x_q and y_p == y_q): pequalq = True

    if pequalq: lda = ((3*(x_p**2) + a) * modinv(2*y_p,module)) % module
    else: lda = ((y_q - y_p) * modinv(x_q - x_p,module)) % module

    
    x_s = ((lda ** 2) - x_p - x_q) % module
    y_s = ((-y_p) + lda*(x_p - x_s)) % module

    print("Lambda = " + str(lda))
    print("xs = (" + str(x_s) + "," + str(y_s) + ") with point P = ({},{}) and Q = ({},{})".format(x_p,y_p,x_q,y_q))
    return x_s,y_s

def decomposeZ(x):
    powers = []
    i = 1
    while i <= x:
        if i & x:
            powers.append(i)
        i <<= 1
    return powers


def CalculateP_list(x_p,y_p,a,module):
    p_list = []
    p_list.append([x_p,y_p])
    print("1P = (" + str(x_p) + "," + str(y_p) + ")\n\n")
    counter = 1
    while counter < 10:
        lastp = p_list[-1]
        x_s,y_s = calculateSum(lastp[0],lastp[1],lastp[0],lastp[1],module,a)
        print(str(2*counter) + "P = ("+str(x_s)+","+ str(y_s) + ") \n\n")
        p_list.append([x_s,y_s])
        counter+=1;
    return p_list


if __name__ == '__main__':
    print("Calculates the DoubleAndAdd algorithm for E_p(a,b)")
    x_p= int(input("Insert x_p: "))
    y_p= int(input("Insert y_p: "))
    a = int(input("Insert a: "))
    module = int(input("Insert module: "))
    k = int(input("Insert k: "))

    p_Doublelist = CalculateP_list(x_p,y_p,a,module)
    print("------------------ Calculating KP ---------------------------")
    p_list = [[0,0]]
    for i in decomposeZ(k):
        last = p_list[-1]
        iP = p_Doublelist[i-1]
        p_list.append(calculateSum(last[0],last[1],iP[0],iP[1],module,a))
        print("")

    print("K*P is: " + str(p_list[-1]))







