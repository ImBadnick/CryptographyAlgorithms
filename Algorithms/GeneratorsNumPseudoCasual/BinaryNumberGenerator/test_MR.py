import checkN
import random

def process(N,k):
    for i in range(k):
        y = random.randint(2, N - 1)
        if checkN.verifica(N,y) == False: return False
    return True


if __name__ == '__main__':
    try:
        N = int(input("Insert N: "))
        k = int(input("Insert K: "))
    except ValueError:
        print("Input is not an integer!")
        exit(0)

    prime = process(N,k)
    prob = (1/4)**k
    if prime: print("The number is prime with prob of: " + str(prob))
    else: print("The number is not prime with prob of 100%")
