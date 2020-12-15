import math

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount


if __name__ == '__main__':
    print("The program checks if g is a cyclic generator for the module")
    g = int(input("Insert g: "))
    module = int(input("Insert module: "))
    phi_module = phi(module)
    print("phi(module) = " + str(phi_module))
    g_kList = []
    for k in range(phi(module)): #finds the g_k = (g**k)%module
        k+=1
        g_k = (g**k)%module
        print("K = {} -> {}^{} mod {} = {}".format(k,g,k,module,g_k))
        g_kList.append(g_k)

    test = True
    for i in range(module-1): #checks if all the values [1,module-1] can be generated
        i+=1
        if(not i in g_kList):
            print("{} misses".format(i))
            test = False

    print("G is generator? -> " + str(test))
