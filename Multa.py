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


def consultarMultes(fitxer):
    f=open(fitxer)
    linia=f.readline()
    comptador=0
    while linia!="":
        c=linia.split("/")
        comptador+=1
        print "num",comptador,"num matricula->",c[0],"diners a pagar->",c[1]
    f.close()

def logIn():
    us="Agent1"
    pas="policia"
    usuari=input("entri usuari: ")
    password=input("entri contrasenya")
    success=False
    while usuari!=us and password!=pas:
        success=False
        usuari=input("entri usuari: ")
        password=input("entri contrasenya")
    return True
