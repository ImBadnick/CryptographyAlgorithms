import math

def generators(n):
    s = set(range(1, n))
    results = []
    for a in s:
        g = set()
        for x in s:
            g.add((a**x) % n)
        if g == s:
            results.append(a)
    return results



if __name__ == '__main__':
    print("The program prints the generators of Z_n")
    n = input("Insert n:")
    gens = generators(int(n))
    if gens:
        print(f"Z_{n} has generators {gens}")