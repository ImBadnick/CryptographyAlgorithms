from string import ascii_letters

if __name__ == '__main__':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    cripto = input("Insert cripto: ")
    k = 1
    while True:
        msg = ''.join([alphabet[(ascii_letters.index(c) - k) % 26] for c in cripto])
        confirm = input("Is that the right msg? " + msg + " [y] [n]: ")
        if confirm == "y": break
        k = k+1

    print("Msg is: " + msg + " and the key is: " + str(k))