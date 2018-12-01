#!/usr/bin/env python
# -*- coding: utf-8 -*-
import main_lib, random

#Aquesta funció impreix la llista d'opcions
# a triar perquè se't facin preguntes
def printOptionsCalc():
    print "Choose an option:"
    print "[1] Sum"
    print "[2] Subtract"
    print "[3] Mutliplication"
    print "[4] Division"
    print "[5] Coctail"
    print "[6] Quit"

#Aquesta funció et printeja una felicitació aleatòria
def randomCongrat():
    x = random.randint(0,4)
    if(x == 0):
        print("You are right, congratulations!!")
    elif (x == 1):
        print("Ohh Yeah!")
    elif (x == 2):
        print("You are a machine")
    elif (x == 3):
        print("I can see that math is your subject ;)")
    else:
        print("Correct!")

#Aquesta funció printeja un missatge quan has fallat una resposta
def randomSorrow():
    x = random.randint(0,4)
    if(x == 0):
        print("You're wrong!")
    elif (x == 1):
        print("This isn't the answer")
    elif (x == 2):
        print("Sorry, but this is incorrect")
    elif (x == 3):
        print("I hope you get the next one right!")
    else:
        print("Incorrect!")

#Aquesta funció es crida quan has acabat el test o un nombre de preguntes
def finishActivity():
    print ("Okay so, what do you want to do?")
    endActivityOptions()
    return main_lib.askNumberOption("Which option do you want to choose?", 2)

#Funció que printeja les opcions de quan s'ha acabat
#el test o un nombre de preguntes
def endActivityOptions():
    print("[1] Repeat")
    print("[2] Go Back")

#Funció que et deixa triar què vols fer (suma, resta, etc.)
def askOption():
    printOptionsCalc()
    option = main_lib.askNumberOption("Which option do you want to choose? ", 6)
    return option

#Funció que fa els càlculs a partir d'un tipus (+ = suma, - = resta, etc.)
def getAnswerFromType(num1, num2, type):
    if(type == "+"):
        return  num1+num2
    elif(type == "-"):
        return num1-num2
    elif(type == "*"):
        return num1*num2
    else:
        return  num1/num2

#Funció que et pregunta una questió matemàtica
def askQuestion(num1, num2, type):
    print num1, type, num2, "= ",
    answer = raw_input()
    while(not main_lib.checkIfInt(answer)):
        answer = raw_input("Write a correct value: ")
    return int(answer)

#Retorna un tipus d'operació aleatòria
def randomType():
    x = random.randint(0,3)
    if(x == 0):
        return "+"
    elif(x == 1):
        return "-"
    elif(x == 2):
        return "*"
    else:
        return "/"

#Funció que té cura de quan s'entra al mode de
#personalització de preguntes, on et fa el nombre de
#preguntes que dessitges i et diu si les seves respostes són correctes o no
def customQuestions(type):
    endCustom = False
    mainType = type
    while(not endCustom):
        success = False
        numQuestions = 1
        #Et pregunta el nombre de questions que vols que se't facin
        while(not success):
            numQuestions = raw_input("How many questions do you want to be asked? ")
            while(not main_lib.checkIfInt(numQuestions)):
                numQuestions = raw_input("Write a correct value: ")
            if(numQuestions < 1):
                print ("Number of questions cannot be less than 1!")
            else:
                success = True
        numQuestions = int(numQuestions)
        #Es va repetint per fer-te totes les preguntes que tu vols
        i = 0
        while (i < numQuestions):

            if (mainType == "c"):
                type = randomType()

            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            if(type == "*"):
                num1 = random.randint(0,10)
                num2 = random.randint(0, 10)
            elif(type == "/"):
                #En el cas de la divisió, num2 no pot ser 0
                #(no es pot dividir per 0) i faig que el resultat
                #sigui enter ja que si num1%num2 = 0 vol dir que no hi ha residu
                if(num2 == 0):
                    num2 = random.randint(1,10)
                while(num1%num2 != 0):
                    num1 = random.randint(0, 100)
                    num2 = random.randint(1, 10)
            userAnswer = askQuestion(num1, num2, type)
            answer = getAnswerFromType(num1, num2, type)
            if (userAnswer == answer):
                randomCongrat()
            else:
                randomSorrow()
                print "The correct answer was", answer
            i+=1

        option = finishActivity()
        if(option == 2):
            endCustom = True
    askToTeach()            #Torna a la pantalla inicial

#Funció que té cura de fer exàmens de 10 preguntes
def test(type):
    endTest = False
    mainType = type
    while(not endTest):
        numQuestions = 10
        points = 0
        i=0
        while(i < numQuestions):
            if(mainType == "c"):
                type = randomType()

            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            if (type == "*"):
                num1 = random.randint(0, 10)
                num2 = random.randint(0, 10)
            elif(type == "/"):
                if (num2 == 0):
                    num2 = random.randint(1, 10)
                while (num1 % num2 != 0):
                    num1 = random.randint(0, 100)
                    num2 = random.randint(1, 10)

            answer = askQuestion(num1, num2, type)
            if(answer == getAnswerFromType(num1,num2,type)):
                points += 1
            i+=1
        print "The test has finished!"
        print "Your puntuation is", points, "/10"
        if(finishActivity() == 2):
            endTest = True
    askToTeach()            #Torna a la pantalla inicial

#Funció que et fa triar si vols un exàmen, preguntes personalitzades o tornar enrere
def askOperationOptions(type):
    print "You have choosen " + type + "!"
    operationOptions()
    return main_lib.askNumberOption("Which option do you want to choose? ", 3)

#Printeja les opcions que tens un com has entrat a un tipus d'operació
def operationOptions():
    print "[1] Custom questions"
    print "[2] Test"
    print "[3] Go Back"

#Crida les funcions necessàries per fer la suma
def teachSum():
    option = askOperationOptions("Sum")
    if(option == 1):
        customQuestions("+")
    if(option == 2):
        test("+")
    if(option == 3):
        askToTeach()
#Crida les funcions necessàries per fer la resta
def teachSubstract():
    option = askOperationOptions("Substract")
    if(option == 1):
        customQuestions("-")
    if(option == 2):
        test("-")
    if(option == 3):
        askToTeach()
#Crida les funcions necessàries per fer la multiplicació
def teachMultiplication():
    option = askOperationOptions("Multiplication")
    if(option == 1):
        customQuestions("*")
    if(option == 2):
        test("*")
    if(option == 3):
        askToTeach()
#Crida les funcions necessàries per fer la divisions
def teachDivision():
    option = askOperationOptions("Division")
    if(option == 1):
        customQuestions("/")
    if(option == 2):
        test("/")
    if(option == 3):
        askToTeach()

# Crida les funcions necessàries per fer la divisions
def teachCoctail():
    option = askOperationOptions("Coctail   ")
    if (option == 1):
        customQuestions("c")
    if (option == 2):
        test("c")
    if (option == 3):
        askToTeach()

#Fució principal d'aquesta llibreria
def askToTeach():
    main_lib.displayTitle("Welcome to your automatic math teacher!")
    userOption = askOption()
    if(userOption == 1):
        teachSum()
    elif(userOption == 2):
        teachSubstract()
    elif (userOption == 3):
        teachMultiplication()
    elif (userOption == 4):
        teachDivision()
    elif (userOption == 5):
        teachCoctail()
    else:
        print "See you another time!!"
        return False


