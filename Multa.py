from getpass import getpass

Usuari = "Agent1"
Password = "policia"

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
        print comptador,". num matricula->",c[0],"diners a pagar->",c[1]
    f.close()

def logIn():

    usuari=input("Entri usuari: ")
    password=getpass("Entri contrasenya: ")
    while usuari!=Usuari and password !=Password:
        print "Usuari o contrasenya no correctes"
        usuari=input("Entri usuari: ")
        password=getpass("Entri contrasenya: ")

    return True
