import string, random

def randomChoiceString (word):
    """
    Retorna una lletra aleatoria de la string que se li passa
    """
    c = random.randint(0, len(word)-1)
    return word[c]

def chequejaParaula (p):
    """
    Chequeja si la paraula es alfabetica i nomes conte minuscules
    >>> chequejaParaula('')
    False
    >>> chequejaParaula('inf0rmatica')
    False
    >>> chequejaParaula('info12be')
    False
    >>> chequejaParaula('nose@e')
    False
    >>> chequejaParaula('aa')
    False
    >>> chequejaParaula('A')
    False
    """
    if len(p) == 0:
        return False
    lused = ""
    for c in p:
        if(c not in string.lowercase):
            return False
        if(c in lused):
            return False
        else:
            lused+=c
    return True

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

def askWord():
    """
    Demana una paraula indefinidament fins que s'introdueix
    una paraula que conte nomes lletres minuscules i no repeteix lletres
    """
    gotWord = False
    while not gotWord:
        word = raw_input("Write a word: ")
        if (chequejaParaula(word)):
            gotWord = True
        else:
            print "Bad word including not lower alphabetical letters or repeating characters"
    return word

def askNumberOption(question, numbers):
    """
    Demana una pregunta (parametre 1) on es poden triar opcions del 1 al parametre 2 (numbers)
    i retorna el que l'usuari ha triat
    """
    while(True):
        answerUser = raw_input(question)
        while(not checkIfInt(answerUser)):
            answerUser = raw_input("Write a valid answer: ")
        answerUser = int(answerUser)
        if(answerUser > 0 and answerUser <= numbers):
            return answerUser

def askYorNQuestion(question):
    """
    Fa una pregunta de si o no
    """
    while (True):
        answerUser = raw_input(question + "(Y/N) ")
        if (answerUser == "N" or answerUser == "n"):
            return False
        if (answerUser == "Y" or answerUser == "y"):
            return True
