from string import ascii_letters

if __name__ == '__main__':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    msg = input("Insert msg: ")
    try: k   = int(input("Insert k: "))
    except ValueError:
        print("Input not an integer")
        exit(0)
    cripto = ''.join([alphabet[(alphabet.index(c) + k) % 26] for c in msg])

    print("Cripto: " + cripto)