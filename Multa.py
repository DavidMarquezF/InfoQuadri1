#!/usr/bin/env python
# -*- coding:utf-8 -*-
from getpass import getpass
import img2char, os.path, sys


Usuari = "Agent1"
Password = "policia"

#--------------------Funcionalitat general

def displayTitle(title):
    """
    Escriu un títol
    """
    print
    lengthTitle = len(title) + 8
    print ("\t" + "*"*lengthTitle)
    print ("\t" + "*** " + title + " ***")
    print ("\t" + "*"*lengthTitle)
    print

def menu():
    displayTitle("MENU")
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
        print str(comptador) +". Matricula: ",c[0],"    Multa: ",c[1],
    print
    f.close()

def logIn():
    """
    Log in pel policia
    """
    displayTitle("LOGIN")
    usuari=raw_input("Entri usuari: ")
    password=getpass("Entri contrasenya: ")
    while usuari!=Usuari and password !=Password:
        print "Usuari o contrasenya no correctes"
        usuari=raw_input("Entri usuari: ")
        password=getpass("Entri contrasenya: ")

    print "Login correcte! \n"
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
    for linia in range(len(listTxt)-1):
        listTxt[linia ]+="\n"
    f.writelines(listTxt)
    f.close()

def diccionari(fitxer):
    """
    Retorna un diccionari on l'index es la matricula
    """
    d={}
    f=open(fitxer,"r")
    for linia in f:
        x=linia.find("\n")
        l=linia[:x]
        if x<0:
            l=linia

        g=l.split("/")
        d[g[0]]=int(g[1])
    return d



#---------------------Afegir Multa
def askFile():
    """
    Demana el fitxer
    """
    while True:
        f = raw_input("Introdueixi el fitxer amb la matricula: ")
        if(os.path.isfile(f)):
            return f
        else:
            print f + " no es un fitxer"

def askFee():
    """
    Demana la multa
    """
    while True:
        fee = raw_input("Introdueixi la multa (en euros): ")
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

def demanaMatricula():
    """
    Retorna la matricula que s'ha demanat, iteria si no és correcte
    """
    while True:
        matricula = raw_input("Introdueix matricula: ")
        if(checkIfInt(matricula)):
            return matricula
        else:
            print "Matricula incorrecte."

def eliminaMatricula(fitxer):
    """
    Retorna el diccionari del fitxer sense la matricula que es vol eliminar
    """
    matricula=demanaMatricula()
    d=diccionari(fitxer)
    if d.has_key(matricula):
        del d[matricula]
        print "Multa eliminada exitosament!\n"
    else:
        print "Matricula no registrada."
    return d



#-----------------------Gestiona opcions

def selectOption(op, patr,multesFile):
    if(op == 1):
        displayTitle("AFEGIR MULTA")
        dic = diccionari(multesFile)
        af = afegirMulta(patr, dic)
        writeToFile(multesFile, dicToString(af))
        print "Multa afegida exitosament!\n"
    elif(op == 2):
        displayTitle("ELIMINAR MULTA")
        consultarMultes(multesFile)
        print
        el = eliminaMatricula(multesFile)
        writeToFile(multesFile, dicToString(el))
    elif(op == 3):
        displayTitle("CONSULTAR MULTES")
        consultarMultes(multesFile)
        raw_input("Apreta Enter per tornar al menu...")
    elif(op == 4):
        exit()

if(__name__ == "__main__"):
    logIn()
    s = sys.argv[1:]
    patrons = s[0]
    multesFile = s[1]
    if (not os.path.isfile(multesFile)):
        print multesFile + " no es un fitxer i per tant no es pot seguir fent operacions"
        exit()

    while True:
        menu()

        selectOption(askNumberOption("Seleccioni una opcio: ", 4), patrons, multesFile)