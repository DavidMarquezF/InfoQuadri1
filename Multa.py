from getpass import getpass
import img2char, os.path, sys


Usuari = "Agent1"
Password = "policia"

#--------------------Funcionalitat general

def menu():
    print "[1] Afegir multa"
    print "[2] Eliminar multa"
    print "[3] Mostrar multes"
    print "[4] Exit"

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

#------------------Consulta Multes

def consultarMultes(fitxer):
    """
    Mostra multes per pantalla
    """
    f=open(fitxer)

    comptador=0
    for linia in f:
        c=linia.split("/")
        comptador+=1
        print str(comptador) +". Matricula: ",c[0],"    Multa: ",c[1]
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


#------------------------Elimina Multa





#-----------------------Gestiona opcions

def selectOption(op, patr,multesFile):
    if(op == 1):
        dic={}#---------------------------------
        afegirMulta(patr, dic)
        print "Multa afegida exitosament!\n\n"
    elif(op == 2):
        pass
    elif(op == 3):
        consultarMultes(multesFile)
        raw_input("Apreta Enter per tornar al menu...")
    elif(op == 4):
        exit()

if(__name__ == "__main__"):
    s = sys.argv[1:]
    patrons = s[0]
    multesFile = s[1]
    if (not os.path.isfile(multesFile)):
        print multesFile + " no es un fitxer i per tant no es pot seguir fent operacions"
        exit()

    while True:
        menu()

        selectOption(askNumberOption("Seleccioni una opcio: ", 4), patrons, multesFile)