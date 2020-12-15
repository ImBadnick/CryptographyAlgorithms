import sys
import bss
import test_MR

def process():
    blist = bss.process()
    blist.insert(0,1)
    blist.append(1)
    N = int("".join(str(x) for x in blist), 2)
    while test_MR.process(N,3) == False:
        N = N +2
    print([int(x) for x in bin(N)[2:]])
    return [int(x) for x in bin(N)[2:]]



if __name__ == '__main__':
    binaryNumber = process()