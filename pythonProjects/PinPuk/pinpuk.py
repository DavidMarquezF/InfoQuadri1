#!/usr/bin/env python
# -*- coding: utf-8 -*-
from getpass import getpass
from main_lib import *
import sys, time, calculateTeacher, main_lib

#Definició de variables globals
PIN = 1234          #El PIN que l'usuari ha d'entrar
PUK = 123456789     #El Puk que l'usuari ha d'entrar
IntentsPIN = 3      #Nombre d'intents per encertar el PIN
IntentsPUK = 5      #Nombre d'intents per encertar el PUK
UserEmail = "David" #Email per entrar al mòbil
UserPass = "1234"   #Contrasenya per entrar al mòbil


#Fa esperar uns segons i mostra per pantalla quan et queda
def waitForTime(timeWait):
    iterations = 0
    while(iterations < timeWait):
        sys.stdout.write("\r" + "Try again in " + str(timeWait-iterations) + " seconds")#sys.stoud.write no salta de línia. \r s'utilitza per tornar a l'inici de la línia i per tant sobreescriurà el que hi havia
        sys.stdout.flush()  #Obliga mostrar el que hi ha guardat al buffer, ja que la funció python stdout és buffejada
        time.sleep(1)
        iterations+=1
    sys.stdout.write("\r\033[K")    #Retorna a l'inici de  línia i borra la línia

#Funció que demana login al mòbil
def askForLogin(intents, tempsEspera):
    while True:
        i = 0
        while(i < intents):
            email = raw_input("Email: ")
            password = getpass("Password: ")
            if(email == UserEmail and password == UserPass):
                return True
            else:
                print "The password or the email are wrong"
                print "You have", intents-(i+1), "tries left"
            i+=1

        print "Exceeded maximum number of iterations"
        waitForTime(tempsEspera)


#Funció Que pregunta si es vol obrir el navegador
def askOpenWebBrowser():
    if(askYorNQuestion("Do you want to open the web browser? ")):
        print "Opening web browser, wait for a moment please"
        time.sleep(1)
        openWebBrowser("https://www.ecosia.org/")
    else:
        initMobile()


#Funció que demana el PIN
def askPin():
    i= 0
    pinCorrect = False
    while(i < IntentsPIN and not pinCorrect):
        pin = getpass("Enter PIN code: ")
        while(not checkIfInt(pin)):
            pin = getpass("Enter a valid PIN code: ")
        pin = int(pin)
        if(pin == PIN):
            pinCorrect = True
        i += 1

    if(pinCorrect):
        print "Unblocked SIM. Welcome."
    else:
        print "Blocked SIM."
    return pinCorrect

#Funció que demana el PUK
def askPuk():
    j=0
    pukCorrect = False
    while(j < IntentsPUK and not pukCorrect):
        puk = getpass("Enter PUK code: ")
        while(not checkIfInt(puk)):
            puk = getpass("Enter a valid PUK code: ")
        puk = int(puk)
        if(puk == PUK):
            pukCorrect = True
        else:
            print "Incorrect.", 5- (j+1),  "available requests"
        j+=1
    if(not pukCorrect):
        print IntentsPUK, "wrong PUK codes. Blocked SIM."
    else:
        print "Unblocked SIM. Welcome"
        return True

def mobileOptions():
    print "[1] Open Web browser"
    print "[2] Open math teacher"

def initMobile():
    displayTitle("Welcome to your mobile phone. Enjoy!")
    print getTime()
    print getDate()
    mobileOptions()
    answer = main_lib.askNumberOption("Which option do you choose? ", 2)
    if (answer == 1):
        askOpenWebBrowser()
    else:
        if(not calculateTeacher.askToTeach()):
            initMobile()

if(__name__ == "__main__"):
    if(askPin() or askPuk()):
        if(askForLogin(3, 5)):
           initMobile()







