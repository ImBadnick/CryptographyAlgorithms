if __name__ == '__main__':
    cripto = input("Insert cripto: ")
    key = input("Insert key: ")
    print("Cripto: " + cripto + " and key: " + key)
    ncripto = int(cripto,2)
    nkey = int(key,2)
    msg = ncripto ^ nkey
    print(('msg is: {0:08b}=' + str(msg) + ' with cripto = ' + str(ncripto) + ' and key = ' + str(nkey)).format(msg))