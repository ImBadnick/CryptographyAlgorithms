def printList(l,listname):
    print(listname + " values:", end=' ')
    for j in range(len(l)):
        print(l[j], end=' ')
    print("")

def decomposeZ(x):
    powers = []
    i = 1
    while i <= x:
        if i & x:
            powers.append(i)
        i <<= 1
    return powers

def calculateY_2_J(y,max,S):
    listY_2_J = []
    i = 0
    while 2**i <= max:
        listY_2_J.append((y**(2**i)) % S)
        i = i+1
    return listY_2_J

def calculateX(powers,y, S):
    list = []
    x = 1
    for value in powers:
        x = (x * (y**int(value))) % s
    return x%S

def repeatSigntoString(list,sign):
    repeatString = str(list[0])
    for i in range(len(list)-1):
        repeatString = repeatString + " " + sign + " " + str(list[i+1])
    return repeatString

if __name__ == '__main__':
    print("The algorithm bases on calculate x = (y^z) mod s with SuccessiveQuadratures method")
    try:
        y = int(input("Insert y: "))
        z = int(input("Insert z: "))
        s = int(input("Insert s: "))
    except ValueError:
        print("Input is not an integer!")
        exit(0)

    powers = decomposeZ(z)
    printList(powers,"DecomposeZ List")

    y_2_j = calculateY_2_J(y,int(powers[-1]),s)
    counter = 0;
    for value in y_2_j:
        print("{}^{} mod {} = {}".format(y,2**counter,s,value))
        counter+=1

    x = calculateX(powers,y, s)
    print(("x value = {}^{} mod {} = " + str(x)).format(y,z,s))