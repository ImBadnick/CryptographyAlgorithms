import sympy

def printList(l,listname):
    print(listname + " values:", end=' ')
    for j in range(len(l)):
        print(l[j], end=' ')
    print("")

def VerifyInput(p,q):
    if ((p%4)==3 and (q%4)==3):
        cond1 = True
    else:
        print("condition 1 problem")
        cond1 = False

    if(sympy.isprime(2*(p//4)+1) and sympy.isprime(2*(q//4)+1)):
        cond2 = True
    else:
        print("condition 2 problem")
        cond2 = False

    return (cond1 and cond2)


def process():
    print("The algorithm bases on n=p*q, y=a number, x(0) = y^2 mod n, x(i)=x(i-1)^2 mod n, b(i)=1 <=> x(m-1) odd ")
    try:
        p = int(input("Insert p: "))
        q = int(input("Insert q: "))
        y = int(input("Insert y: "))
    except ValueError:
        print("Input is not an integer!")
        exit(0)
    if (VerifyInput(p, q)):
        print("p and q are correct")
    else:
        print("p and q are not correct")
        exit(0)
    n = p*q;
    print("n value = " + str(n))
    x_0 = (y**2 % n)
    print("Seed value = " + str(x_0))
    xlist = []
    xlist.append(x_0)
    blist = []
    blist.append(x_0%2)
    try:
        nbits = int(input("How much random bits you want? ")) - 1
    except ValueError:
        print("Input is not an integer!")
    i = 0
    while i<nbits:
        x_i = int((xlist[-1]**2)) % n
        xlist.append(x_i)
        blist.append(x_i % 2)
        i = i+1

    printList(xlist, "x")

    blist.reverse()
    printList(blist, "bit")

    return blist

if __name__ == '__main__':
    blist = process()




