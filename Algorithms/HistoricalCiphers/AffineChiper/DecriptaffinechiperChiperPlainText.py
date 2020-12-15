import math

def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 


def modinv(a, m): 
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None  # modular inverse does not exist 
    else: 
        return x % m 



if __name__ == '__main__':
    print("Prints all the possible msg from a cryptogram ")
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    try:
        cripto = input("Insert cripto: ")
        search = input("Insert msg searched: ")
    except ValueError:
        print("Value not an integer")
        exit(0)

    a = 1
    confirm = 'n'
    while a<=26:
        b = 1
        while b <= 26:
            if math.gcd(a, 26) == 1:
                msg = ''.join([alphabet[(int(modinv(a,26) * (alphabet.index(c) - b)) % 26)]
                     if c in alphabet else c for c in cripto])
                print(a, b,msg)
                if(msg == search): break
                b = b+1
            else:
                b = b+1
                print("mcd(a,26)!=1")
                break
        a = a+1
        if msg == search: break
