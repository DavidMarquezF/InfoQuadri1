#!/usr/bin/env python
# -*- coding: utf-8 -*-

##AQUESTA ÉS LA LLIBRERIA PRINCIPAL QUE CONTÉ FUNCIONS BÀSIQUES
from datetime import datetime
import webbrowser

#Mira si el valor que li passes és un int
def checkIfInt(number):
    try:                #Prova de fer això
        int(number)
        return True
    except ValueError:  #Si dona error retorna False
        return False

#Funció que crea una pregunta de Sí o No i retorna la resposta
def askYorNQuestion(question):
    while (True):
        answerUser = raw_input(question + "(Y/N) ")
        if (answerUser == "N" or answerUser == "n"):
            return False
        if (answerUser == "Y" or answerUser == "y"):
            return True

#Espera la resposta d'una llista d'opcions del 1 a qualsevol nombre (parametre numbers)
def askNumberOption(question, numbers):
    while(True):
        answerUser = raw_input(question)
        while(not checkIfInt(answerUser)):
            answerUser = raw_input("Write a valid answer: ")
        answerUser = int(answerUser)
        if(answerUser > 0 and answerUser <= numbers):
            return answerUser

#Retorna l'hora, minuts i segons
def getTime():
    return datetime.now().strftime("%H:%M:%S")

#Retorna la data
def getDate():
    return datetime.now().strftime("%d/%m/%Y")

#Obre un navegador amb l'url que se li passa
def openWebBrowser(url):
    webbrowser.open_new_tab(url)

#Fa aparèixer un títol: Una línia d'esteriscs, una altra pel títol i una altre d'esteriscs
def displayTitle(title):
    lengthTitle = len(title) + 8
    print ("\t" + "*"*lengthTitle)
    print ("\t" + "*** " + title + " ***")
    print ("\t" + "*"*lengthTitle)