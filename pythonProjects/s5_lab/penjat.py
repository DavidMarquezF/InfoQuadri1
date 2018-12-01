from getpass import getpass
import string

def chequejaParaula (p):
    """
    Chequeja si la paraula es alfabetica
    >>> chequejaParaula('')
    False
    >>> chequejaParaula('infOrmatica')
    True
    >>> chequejaParaula('info12be')
    False
    >>> chequejaParaula('nose@e')
    False

    """
    if len(p) == 0:
        return False

    for c in p:
        if(c not in string.letters):
            return False
    return True

def paraulaCorrecta():
    """
    retorna la paraula correcta del jugador1. Itera mentre no es correcta

    """
    t = False
    while not t:
        jugador1 = getpass("Enter word player 1: ")
        t = chequejaParaula(jugador1)
        if not t:
            print "Enter a valid word."
    return jugador1.upper()

def chequejaLletra(l):
    """
    retorna si la lletra es correcta

    >>> chequejaLletra('')
    False
    >>> chequejaLletra('as')
    False
    >>> chequejaLletra('3')
    False
    >>> chequejaLletra('#')
    False
    >>> chequejaLletra('b')
    True
    """
    return len(l) == 1 and l in string.letters

def demanarLletra():
    """
    retorna la lletra correcta. Itera mentre no correcta

    """
    t = False
    while not t:
        lletra = raw_input("Enter letter: ")
        t = chequejaLletra(lletra)
        if(not t):
            print "Bad letter"

    return lletra.upper()

def endevinantParaula(original, oculta, l):
    """
    retorna la paraula a mig endevinar actualitzada
    >>> endevinantParaula('informe', '@@@@@@@', 'r')
    '@@@@r@@'
    >>> endevinantParaula('informe', '@@@@r@@', 'e')
    '@@@@r@e'

    """
    s = ""
    i = 0
    for lletra in original:
        if (lletra == l):
            s += l
        else:
            s += oculta[i]
        i += 1
    return s

def jugar(opor):
    print "Player 2. Your turn: "
    oculta = "@" * len(j1)
    print oculta
    j = 0
    while oculta != j1 and j < opor:
        l = demanarLletra()
        oculta = endevinantParaula(j1, oculta, l)
        print oculta
        j += 1

    if (oculta == j1):
        print "The winner is player 2!"
    else:
        print "The winner is player 1! The word was", j1
def menuOpcions():
    opcio = "2"
    while opcio != "0" and opcio != "1":
        print "[1] Play"
        print "[0] Exit"
        opcio = raw_input("Enter opcion: ")
    return opcio



if __name__ == "__main__":
    Oportunitats = 13
    tria = menuOpcions()
    while tria != "0":
        print "Guess the word"
        j1 = paraulaCorrecta()
        jugar(Oportunitats)
        tria = menuOpcions()






