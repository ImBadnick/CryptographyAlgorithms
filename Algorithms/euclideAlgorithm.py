def Extended_Euclid(a,b):
    if b == 0:
        print("EE({},{}) = <{},{},{}>".format(a, b,a,1,0))
        return a,1,0
    else:
        _d_,_x_,_y_ = Extended_Euclid(b,a%b)
        d = _d_
        x = _y_
        y = _x_ - (a//b)*_y_
        print("EE({},{}) = <{},{},{}>".format(a,b,d,x,y))
        return d,x,y


if __name__ == '__main__':
    print("Calculates the Extended_Euclid algorithm to find the inverse module")
    x = int(input("Insert x: "))
    module = int(input("Insert module: "))

    d,inv,y = Extended_Euclid(x,module)
    print("The inverse of {} is {}".format(x,inv))