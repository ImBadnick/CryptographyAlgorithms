class point:
 def __init__(self, x, y):
        self.x = x
        self.y = y


def quadraticResidues(module):
    quadraticresidues = []
    for i in range(module):
        quadraticresidues.append(point(i,(i**2) % module))
    return quadraticresidues



if __name__ == '__main__':
    print("Transform m into a point of the elliptic curve E_p(a,b) - Kobritz algorithm")
    m= int(input("Insert m: "))
    h= int(input("Insert h: "))
    a = int(input("Insert a: "))
    b = int(input("Insert b: "))
    module = int(input("Insert module: "))

    if not ((m+1)*h < module):
        print("False condition (m+1)*h < p ")
        exit(0)

    quadraticresidues = quadraticResidues(module)
    pm = -1
    for x in range(h):
        _x_ = m*h + x
        y_2 = ((_x_ ** 3) + a * _x_ + b) % module
        print("i = {} -> x = {} , y^2 = {}".format(x,_x_,y_2))
        for p in quadraticresidues:
            if(y_2 == p.y):
                pm = point(_x_,(y_2)**(1/2))

    if(pm == -1):
        print("m coding not found")
    else: print("Pm = " + pm.__dict__)