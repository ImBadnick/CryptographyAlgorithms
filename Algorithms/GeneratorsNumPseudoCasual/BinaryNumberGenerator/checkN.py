import random
import math

def printList(l,listname):
    print(listname + " values:", end=' ')
    for j in range(len(l)):
        print(l[j], end=' ')
    print("")


def calculateWandZ(n):
    i = 2
    max = 0
    while i<=n:
        if(n%(2**i)==0): max = i
        i = i+1
    return max, (n/(2**max))


def verifica(N,y):
    w, z = calculateWandZ(N - 1)
    print("w values is = " + str(w) + " , z value is = " + str(z))
    print("Y value is = " + str(y))

    mcd = math.gcd(N,y)
    if (mcd == 1):
        condition1 = True
        print("condition1 is True: MCD(N,y) = 1")
    else:
        condition1 = False
        print("condition1 is False: MCD(N,y) = " + str(mcd))

    condition2p1 = False
    firstCond = (y ** z) % N
    if  firstCond == 1:
        condition2p1 = True
    print("condition2p1 is " + str(condition2p1) + ": (y^z) mod N = " + str(firstCond) )

    condition2p2 = False
    tmpList = []
    tmpList.append(y**z % N)
    for i in range(0,w):
        tmp = int(tmpList[-1])
        if tmp == N-1:
            condition2p2 = True
            break
        tmpList.append(tmp ** 2 % N)
    print("condition2p2 is " + str(condition2p2), end=' ')
    printList(tmpList,"")

    return condition1 and (condition2p1 or condition2p2)


def findK(prob):
    k = 1
    while True:
        if((1/4)**k <= prob): return k
        k = k+1

def findYs(N,k):
    i = 0
    yList = []
    while i<k:
        y = random.randint(2, N - 1)
        if(y in yList): continue
        if(verifica(N,y)):
            yList.append(y)
            i = i+1
    return yList



if __name__ == '__main__':
    print("The algorithm bases on check if number N is prime with x probability")
    try:
        n = int(input("Insert N: "))
        y = input("Insert y if you know or just press enter: ")
        prob = input("Insert probability if you know or just press enter: ")
    except ValueError:
        print("Input is not an integer!")
        exit(0)

    if y:
        try:
            y = int(y)
        except ValueError:
            print("Input y is not an integer!")
            exit(0)
        if verifica(n,y):
            print("y can be used to check if N is prime or not")

    else:
        if prob:
            num,den = prob.split('/')
            try:
                prob = (int(num)/int(den))
            except ValueError:
                print("Input num and den are not integer!")
                exit(0)

            k = findK(prob)
            print("y values to find: " + str(k))
            yList = findYs(n,k)
            printList(yList,"yList")





