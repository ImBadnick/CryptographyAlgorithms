import math
from functools import reduce

def printList(l,listname):
    print(listname + " values:", end=' ')
    for j in range(len(l)):
        print(l[j], end=' ')
    print("")

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def checkParams(a,b,m):
    condition1 = False
    condition2 = True

    if(math.gcd(b,m) == 1): condition1 = True

    for element in factors(m):
        if(((a-1)%m)!=0): condition2 = False

    if(m%4 == 0):
        if((a-1)%4 == 0): condition3 = True
        else: condition3 = False
    else:
        condition3 = True

    return condition1 and condition2 and condition3

if __name__ == '__main__':
    print("The algorithm uses linearGenerator to generates n bits")
    try:
        a = int(input("Insert a: "))
        b = int(input("Insert b: "))
        m = int(input("Insert m: "))
        seed = int(input("Insert seed: "))
        nbits = int(input("Insert number of bits you want: "))
    except ValueError:
        print("Input is not an integer!")
        exit(0)

    if checkParams(a,b,m):
        print("Params are ok")
    else:
        print("Params error")
        exit(0)

    xlist = []
    xlist.append(seed)
    for i in range(nbits-1):
        xlist.append((a*int(xlist[-1])+b) % m)

    printList(xlist,"xlist")
