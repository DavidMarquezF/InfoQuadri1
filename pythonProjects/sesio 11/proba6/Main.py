#estructura GRUP: Dict(id) = titol, [(alumnes)], nota
#estructura ALUMNE: Dict(nom,cognom) = [grupsid]

#FUNCIONS BASIQUES------------------------------------------------------------------------------------------------------
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
def checkIfFloat(number):
    """
    Chequeja si la string que es passa es un int
    >>> checkIfFloat('10.5')
    True
    >>> checkIfFloat('1A')
    False
    >>> checkIfFloat('asd')
    False
    """

    try:                #Prova de fer aixo
        float(number)
        return True
    except ValueError:  #Si dona error retorna False
        return False

def askYorNQuestion(question):
    """
    Fa una pregunta de si o no
    """
    while (True):
        answerUser = raw_input(question + "(Y/N): ")
        if (answerUser == "N" or answerUser == "n"):
            return False
        if (answerUser == "Y" or answerUser == "y"):
            return True
        print answerUser,"no es una opcio valida."


def askNumberOption(question, numbers, oPermitted = False):
    """
    Demana una pregunta (parametre 1) on es poden triar opcions del 1 al parametre 2 (numbers)
    i retorna el que l'usuari ha triat
    """
    while(True):
        answerUser = raw_input(question)
        while(not checkIfInt(answerUser)):
            answerUser = raw_input("Write a valid answer: ")
        answerUser = int(answerUser)
        if(not oPermitted):
            if(answerUser > 0 and answerUser <= numbers):
                return answerUser
        else:
            if(answerUser >= 0 and answerUser < numbers):
                return answerUser

#DICCIONARIS DES DE FITXER----------------------------------------------------------------------------------------------

def diccionariAlumnes():
    """
    Retorna un diccionari amb els alumnes de clau i una llista dels grups que formen part
    """
    f = open("alumnes.txt")
    d={}
    if(fileIsEmpty("alumnes.txt")):
        return {}
    for line in f:
        s = line.split()
        d[(s[0], s[1])] = s[2:]
    f.close()
    return d

def diccionariDeGrups():
    """
    Retorna un diccionari amb l'id de grup de clau i una llista amb el nom del grup, llista de membres i nota
    """
    f = open("grups.txt")
    d={}
    for line in f:
        s = line.split("/")
        alumnesStr = s[2].split(":")
        alumnes = []
        for alu in alumnesStr:
            alumnes.append(tuple(alu.split()))
        nota = s[3].rstrip()
        d[s[0]] = [s[1], alumnes, nota]
    f.close()
    return d
#HANDLE FILES-----------------------------------------------------------------------------------------------------------

def fileIsEmpty(nom):
    """
    Xequeja si un fitxer esta buit (no hi te res escrit)
    """
    f = open(nom)
    empty = False
    txt =  f.read()
    if (len(txt) == 0 or txt == "\n"):
        empty = True

    f.close()
    return empty

def appendAlumneToFile(nom, alumne):
    """
    Afegeix un alumne nou al fitxer dels alumnes
    """
    f = open(nom, "a")
    text=""
    if(not fileIsEmpty("alumnes.txt")):
        text+="\n"
    text +=alumne[0][0] + " " + alumne[0][1] + " " + str(alumne[1])
    f.write(text)
    f.close()

def writeToFile(nom, text):
    """
    Escriu un text al fitxer desitjat
    """
    f = open(nom, "w")
    f.write(text)
    f.close()

def numberOfLines(nom):
    """
    Retorna el nombre de linies en un fitxer
    """
    f = open(nom)
    l = len(f.readlines())
    f.close()
    return l

#DICT TO STRING---------------------------------------------------------------------------------------------------------
def alumnDictToString(dictAl):
    """
    Passa d'un diccionari d'alumnes a string per poderla posar al fitxer
    >>> alumnDictToString({("David", "Marquez"): ["1","2"]})
    'David Marquez 1 2'
    """
    text =""
    if(dictAl == {}):
        return ""
    lin = len(dictAl.keys())
    i= 0
    for key in dictAl:
        text+=key[0] + " " + key[1]+ " "
        text+=" ".join(dictAl[key])
        if(i < lin - 1):
            text+="\n"
        i+=1
    return text


def grupDictToString(dictGrups):
    """
    Passa d'un diccionari de grups a una string
    >>> grupDictToString({"0":["Fisica", [("Ferran", "Godoy")], "5"]})
    '0/Fisica/Ferran Godoy/5'
    """
    text=""
    separator = "/"
    lin = len(dictGrups.keys())
    zk=0
    for key in dictGrups:
        text+=str(key) + separator   #clau
        text+=dictGrups[key][0] + separator #titol

        l = []
        for i, alumn in enumerate(dictGrups[key][1]):
            l.append(" ".join(alumn))
        text+= ":".join(l) + separator #alumnes

        text+=str(dictGrups[key][2])    #nota
        if(zk < lin - 1):
            text += "\n"
        zk+=1
    return text



#ACTUALITZAR------------------------------------------------------------------------------------------------------------
def actualitzarGrups(alumnes, grups):
    """
    Actualitza els grups(si s'han afegit alumnes, tret, un grup no te membres, etc.)
    """
    grups = checkIfAdded(alumnes,grups)
    grups = checkIfDeleted(alumnes,grups)
    grups = borrarGrupSiBuit(grups)
    return grups

def actualitzarAlumnes(alumnes, grup):
    """
    Actualitza els alumnes (de quins grups formen part)
    """
    alumnesDict = diccionariAlumnes()
    grupsDict = diccionariDeGrups()
    for alumne in alumnes:
        if(alumnesDict[alumne] == ["0"] and str(grup) != "0"):
            alumnesDict[alumne].remove("0")
        alumnesDict[alumne].append(grup)

        if(alumne in grupsDict["0"][1]):
            grupsDict["0"][1].remove(alumne)

    textal = alumnDictToString(alumnesDict)
    writeToFile("alumnes.txt", textal)
    textgr = grupDictToString(grupsDict)
    writeToFile("grups.txt", textgr)

def checkIfAdded(alumnes, grups):
    """
    Mira si s'ha afegit un alumne nou i si es aixi s'afegira al diccionari de grups
    >>> checkIfAdded({("David", "Marquez"): ["1"]},{"1":["Fisica", [("Ferran", "Godoy")], "5"]})
    {'1': ['Fisica', [('Ferran', 'Godoy'), ('David', 'Marquez')], '5']}
    """
    for keyAlum in alumnes:
        for grup in alumnes[keyAlum]:
            if(keyAlum not in grups[grup][1]):
                grups[grup][1].append(keyAlum)
    return grups

def checkIfDeleted(alumnes,grups):
    """
    Mira si s'ha borrat un alumne i el treu del grup si es aixi
    >>> checkIfDeleted({("David", "Marquez"): ["1"]},{"1":["Fisica", [("Ferran", "Godoy"), ('David', 'Marquez')], "5"]})
    {'1': ['Fisica', [('David', 'Marquez')], '5']}
    """
    for key in grups:
        deleteAlum = []
        for i, alumne in enumerate(grups[key][1]):
            if(not alumnes.has_key(alumne)):
                deleteAlum.append(alumne)
        for delA in deleteAlum:
            del grups[key][1][grups[key][1].index(delA)]
    return grups


#ALUMNE-----------------------------------------------------------------------------------------------------------------

def afegirAlumne():
    """
    S'encarrega d'afegir un alumne
    """
    alumnes = diccionariAlumnes()
    while True:
        alumne = crearAlumne()
        if(not alumnes.has_key(alumne)):
            print "Aquest alumne no existex"
        else:
            break
    return alumne

def crearAlumne():
    """
    Demana la informacio per crear un alumne
    """
    while True:
        nom = raw_input("Entra nom: ")
        if(" " in nom or nom ==""):
            print "No hi poden haver espais al teu nom o no pot ser buit"
        else:
            break
    while True:
        cognom = raw_input("Entra cognom: ")
        if(" " in cognom or cognom ==""):
            print "No hi poden haver espais al teu cognom o no pot ser buit"
        else:
            break

    return (nom, cognom)

def eliminarAlumne(alumnesDict, alumne):
    """
    Elimina un alumne del diccionari
    >>> eliminarAlumne({("David", "Marquez"): ["1"], ("Ferran", "Godoy"): ["1"]}, ("Ferran", "Godoy"))
    {('David', 'Marquez'): ['1']}
    """
    del alumnesDict[alumne]
    return alumnesDict

#GRUP-------------------------------------------------------------------------------------------------------------------
def borrarGrupSiBuit(grups):
    """
    Borra un grup si esta buit (no te cap membre)
    >>> borrarGrupSiBuit({"1":["Fisica", [], "5"]})
    {}
    """
    emptyKeys=[]
    for key in grups:
        if(key != "0"):
            if(len(grups[key][1]) == 0):
                emptyKeys.append(key)
    for i in emptyKeys:
        del grups[i]
    return grups

def titolExisteix(titol, grups):
    """
    Comprova si el titol que es vol posar a un grup ja exiteix
    >>> titolExisteix("Fisica",{"0":["Fisica", [("Ferran", "Godoy")], "5"]})
    True
    >>> titolExisteix("Mates",{"0":["Fisica", [("Ferran", "Godoy")], "5"]})
    False
    """
    for item in grups.values():
        if(titol == item[0]):
            return True
    else:
        return False

def afegirGrup():
    """
    Crea i afegeix un grup
    """
    grups = diccionariDeGrups()
    id = str(numberOfLines("grups.txt"))
    while True:
        titol = raw_input("Nom del projecte: ")
        if(titolExisteix(titol, grups)):
            print "Ja existeix un projecte amb aquest nom"
        else:
            break
    alumnes=[]
    print "Entra els alumnes que vols que en formin part:"
    alumnes.append(afegirAlumne())
    while True:
        if(askYorNQuestion("Vol afegir un altre alumne? ")):
            alumne = afegirAlumne()
            if(alumne in alumnes):
                print "Aquest alumne ja ha estat creat"
            else:
                alumnes.append(alumne)
        else:
            break
    nota = "-1"
    grups[id] = [titol, alumnes, nota]
    return [grups,alumnes,id]

#LLISTA GRUP PROJECTES--------------------------------------------------------------------------------------------------

def takeFirst(elem):
    """
    Funcio per fer el filtratge de grups per id
    """
    return elem[0]

def llistaGrupProjectes():
    """
    Llista els grups per ordre de id
    """
    d = diccionariDeGrups()
    val = d.items()
    val = sorted(val,key=takeFirst)

    for elem in val:
        print"-------------------------"
        print elem[0]+"."+elem[1][0]
        print "Membres:",
        for alumn in elem[1][1]:
            print " ".join(alumn)+ ", ",
        print
        print "Nota:",
        if(str(elem[1][2]) == "-1"):
            print "No te nota"
        else:
            print elem[1][2]

#POSAR NOTA-------------------------------------------------------------------------------------------------------------
def printLlistaIDiccionari(d):
    """
    Printeja el titol del grup i la seva nota
    """
    val = d.items()
    val = sorted(val, key=takeFirst)
    di={}
    for elem in val:
        if(elem[0] != "0"):
            print elem[0]+ "." + elem[1][0],"--------- Nota:",
            if (str(elem[1][2]) == "-1"):
                print "No te nota"
            else:
                print elem[1][2]
            di[elem[0]] = elem[1][0]
    return di

def demanarNota():
    """
    Demana la nota que es vol posar a un grup
    """
    while True:
        nota = raw_input("Escriu la nota (0-10): ")
        if(checkIfFloat(nota)):
            if(0<=float(nota)<=10):
                break
            else:
                print "La nota ha de ser entre el 0 i el 10"
        else:
            print "No es un nombre"
    return nota
def posaNota():
    """
    Posa la nota a un grup i ho actualitza al fitxer de grups
    """
    d = diccionariDeGrups()
    dic = printLlistaIDiccionari(d)
    if(len(d.keys()) > 1):
        op = askNumberOption("Esculli el projecte (amb el nombre de davant): ",len(dic))
        print "Ha escollit:",dic[str(op)]
        nota = demanarNota()
        d[str(op)][2] = str(nota)
        text = grupDictToString(d)
        writeToFile("grups.txt", text)
    else:
        print "No hi ha cap grup per posar nota."

#MITJANA NOTES----------------------------------------------------------------------------------------------------------
def sumaDeNotes(d):
    """
    Calcula la suma de totes les notes
    """
    result=0
    counter = 0
    for value in d.values():
        if(str(value[2])!="-1"):
            result+=float(value[2])
            counter+=1
    return [result, counter]

def mitjanaNotes():
    """
    Fa la mitjana de les notes
    """
    d = diccionariDeGrups()
    suma = sumaDeNotes(d)
    print "Hi ha",suma[1],"grups amb nota."
    if(suma[1] == 0):
        print "Per tant no es pot fer la mitjana de les notes."
    else:
        print "La mitjana de les seves notes es:", suma[0]*1.0/suma[1]

#MENU-------------------------------------------------------------------------------------------------------------------

def handleOp(op):
    """
    Fa el que ha de fer depenent de la opcio triada  en el menu principal
    """
    if(op == 1):
        exit()
    elif(op == 2):
        d = diccionariAlumnes()
        alumn = crearAlumne()
        if(alumn not in d):
            appendAlumneToFile("alumnes.txt", [alumn, 0])
        else:
            print "Aquest alumne ja esta creat."
    elif (op == 3):
        aluDic = diccionariAlumnes()
        if (len(aluDic.keys()) > 0):
            grupNou = afegirGrup()
            writeToFile("grups.txt", grupDictToString(grupNou[0]))
            actualitzarAlumnes(grupNou[1], grupNou[2])
        else:
            print "No hi ha cap alumne per poder fer grups"
    elif (op == 4):
        llistaGrupProjectes()
    elif (op == 5):
        posaNota()
    elif (op == 6):
        d = diccionariAlumnes()
        if (len(d.keys()) > 0):
            a = crearAlumne()
            if(d.has_key(a)):
                d = eliminarAlumne(d, a)
                writeToFile("alumnes.txt", alumnDictToString(d))
            else:
                print "Alumne no existent"
        else:
            print "No hi ha cap alumne per esborrar."
    elif (op == 7):
        mitjanaNotes()

def menu():
    """
    Printeja el menu principal
    """
    print "[1] Exit"
    print "[2] Afegir alumne"
    print "[3] Afegir grup de projecte"
    print "[4] Llista grups projecte"
    print "[5] Posar nota"
    print "[6] Esborrar alumne"
    print "[7] Mitjana de projectes"


if(__name__ == "__main__"):
    while True:
        menu()
        handleOp(askNumberOption("Tria una opcio: ", 7))
        grupsDict = diccionariDeGrups()
        alumnDict = diccionariAlumnes()
        writeToFile("grups.txt",grupDictToString(actualitzarGrups(alumnDict,grupsDict)))
