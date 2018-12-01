def checkIfInt(number):
    """
    Chequeja si la string que es passa es un int
    >>> checkIfInt('10')
    True
    >>> checkIfInt('1A')
    False
    >>> checkIfInt('asd')
    False
    """

    try:                #Prova de fer aixo
        int(number)
        return True
    except ValueError:  #Si dona error retorna False
        return False


def askValues(num):
    i = 0
    l = []
    while i < num:
        while True:
            x = raw_input("Write a number: ")
            if(checkIfInt(x)):
                break
            else:
                print "Not a valid number"
        l.append(x)
    return l