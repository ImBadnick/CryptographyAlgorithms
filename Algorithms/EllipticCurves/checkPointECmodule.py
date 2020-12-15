

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
    print("Checks if the point is in the E_p(a,b) and prints all the points of E_p(a,b)")
    x_p= int(input("Insert x_p: "))
    y_p= int(input("Insert y_p: "))
    a = int(input("Insert a: "))
    b = int(input("Insert b: "))
    module = int(input("Insert module: "))

    quadraticresidues = quadraticResidues(module)
    curvePoints = []
    for x in range(module):
        y_2 = ((x**3) + a*x + b) % module
        for p in quadraticresidues:
            if(y_2 == p.y):
                curvePoints.append(point(x,p.x))
    pExists = False
    for p in curvePoints:
        if((x_p % module) == p.x and (y_p % module) == p.y): pExists=True
        print(p.__dict__)

    if(pExists): print("The point exists in the curve")
    else: print("The point doesn't exists in the curve")






