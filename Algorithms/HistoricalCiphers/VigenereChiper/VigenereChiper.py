def split(word):
    return [char for char in word]



if __name__ == '__main__':
    print("Crypts the message with the key inserted")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    try:
        msg = input("Insert msg: ")
        key = input("Insert key: ")
    except ValueError:
        print("Value not an integer")
        exit(0)
    msg = split(msg)
    key = split(key)
    counter = 0
    if (len(msg) > len(key)):
        while (len(msg) > len(key)):
            key.append(key[counter % len(key)])
            counter += 1

    cripto = ''.join([alphabet[(alphabet.index(c) + alphabet.index(k)) % 26 ] for c,k in zip(msg,key)])
    print("cripto = " + cripto)


