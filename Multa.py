from getpass import getpass
import img2char, os.path


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
    """
    Mostra multes per pantalla
    """
    f=open(fitxer)
    linia=f.readline()
    comptador=0
    while linia!="":
        c=linia.split("/")
        comptador+=1
        print comptador,". num matricula->",c[0],"diners a pagar->",c[1]
    f.close()

def logIn():
    """
    Log in pel policia
    """
    usuari=input("Entri usuari: ")
    password=getpass("Entri contrasenya: ")
    while usuari!=Usuari and password !=Password:
        print "Usuari o contrasenya no correctes"
        usuari=input("Entri usuari: ")
        password=getpass("Entri contrasenya: ")

    return True

#---------------------Funcions generals
def dicToString(dic):
    """
    Passa d'un diccionari a una llista de string
    >>> dicToString({"4555":12, "6485":47})
    ['4555/12', '6485/47']
    """
    listText = []
    for key in dic.keys():
        listText.append(key+"/"+str(dic[key]));
    return listText

def writeToFile(file, listTxt):
    f = open(file,"w")
    f.writelines(listTxt)
    f.close()


#---------------------Afegir Multa
def askFile():
    """
    Demana el fitxer
    """
    while True:
        f = raw_input("Introdueixi el fitxer amb la imatge")
        if(os.path.isfile(f)):
            return f
        else:
            print f + " no es un fitxer"

def askFee():
    """
    Demana la multa
    """
    while True:
        fee = raw_input("Introdueixi la multa (en euros)")
        if(checkIfInt(fee)):
            print "Multa de " + fee + " sera afegida a la matricula"
            return int(fee)

def afegirMulta(patr, dic):
    """
    Afegeix una multa a una matricula
    """
    matr = askFile()
    matricula = img2char.nombreMatricula(patr, matr)
    multa = askFee()
    if(dic.has_key(matricula)):
        dic[matricula] += multa
    else:
        dic[matricula] = multa
    return dic





