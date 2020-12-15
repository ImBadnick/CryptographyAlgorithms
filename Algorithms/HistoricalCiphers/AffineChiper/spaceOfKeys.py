import math

if __name__ == '__main__':
    print("Prints the space of keys of affine cipher")
    try:
        module = int(input("Insert module: "))
    except ValueError:
        print("Value not an integer")
        exit(0)

    counter=0
    a = 1
    while a<=module:
        if(math.gcd(a,module)==1): counter=counter+1
        a = a+1

    keynumber = counter*module - 1
    print("key number is: " + str(keynumber))