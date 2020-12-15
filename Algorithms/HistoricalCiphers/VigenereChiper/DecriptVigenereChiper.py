def split(word):
    return [char for char in word]



if __name__ == '__main__':
    print("Decrypt the cryptogram with the key inserted")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    try:
        cripto = input("Insert cripto: ")
        key = input("Insert key: ")
    except ValueError:
        print("Value not an integer")
        exit(0)
    cripto = split(cripto)
    key = split(key)
    counter = 0
    if (len(cripto) > len(key)):
        while (len(cripto) > len(key)):
            key.append(key[counter % len(key)])
            counter += 1

    msg = ''.join([alphabet[(alphabet.index(c) - alphabet.index(k)) % 26 ] for c,k in zip(cripto,key)])
    print("msg = " + msg)


