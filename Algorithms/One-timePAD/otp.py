

if __name__ == '__main__':
    msg = input("Insert message: ")
    key = input("Insert key: ")
    print("Msg: " + msg + " and key:" + key)
    nmsg = int(msg,2)
    nkey = int(key,2)
    cripto = nmsg ^ nkey
    print(('Critpo is: {0:08b}=' + str(cripto) + ' with msg = ' + str(nmsg) + ' and key = ' + str(nkey)).format(cripto))