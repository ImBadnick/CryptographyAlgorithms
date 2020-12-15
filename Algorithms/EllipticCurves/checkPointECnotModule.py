if __name__ == '__main__':
    print("Checks if the point is in the elliptic curve E(a,b)")
    x_p= int(input("Insert x_p: "))
    y_p= int(input("Insert y_p: "))
    a = int(input("Insert a: "))
    b = int(input("Insert b: "))

    if(y_p == (x_p**3 + a*x_p + b)**(1/2)): print("True")
    else: print("false")

