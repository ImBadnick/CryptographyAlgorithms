from itertools import permutations

if __name__ == '__main__':
    cripto = input("Insert cripto: ")
    perms = [''.join(p) for p in permutations(cripto)]
    print(perms)
