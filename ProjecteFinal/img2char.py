import sys, discret, img, imgio,match,split,transf

def getPatr(patrons):
    """
    Obte tots els patrons en blanc i negre
    """
    patronsImg = match.load_patterns(patrons)   #Carrega tots els patrons
    for i, patro in enumerate(patronsImg):
        patronsImg[i] = discret.rgb_to_bn(patro)    #Per a cada patro el converteix en blanc i negre
    return patronsImg

def getMatr(matricula, hPatrons):
    """
    Obte la matricula, la passa a blanc i negre, la retalla verticalment i l'escala
    """
    matriculaImg = imgio.read_rgb(matricula)    #Obte matriu de pixels
    matriculaImg = discret.rgb_to_bn(matriculaImg)  #Ho passa a blanc i negre
    matriculaImg = transf.vtrim(matriculaImg)   #Ho retalla verticalment
    matriculaImg = transf.scale(matriculaImg, hPatrons) #Escala la imatge amb la altura necessaria

    return  matriculaImg


def getMatriculaNumbers(matriculaImg, patronsImg, hasLetters = False):
    """
    Retorna una llista amb cada nombre de la matricula (fa split, match,etc.)
    """
    matriculaNumbers = []
    matriculaSplit = matriculaImg

    i = 0
    while True:
        if(hasLetters): #Si te lletres fara el comptador
            i+=1
            if(i > 4):  # Si ja han passat cuatre nombres es parara
                break

        splt = split.split_digit(matriculaSplit)    #Retalla un nombre i obte el nombre retallat i la resta de la imatge
        if (img.is_null(splt)): #Si el que es retorna es una imatge nula voldra dir que no ha pogut retallar res i per tant es sortira del while
            break
        numSplt = transf.htrim(splt[0]) #Retalla horizontalment(elimina els pixels blancs que hagin pogut sobrar per les bandes)
        matriculaMatch = match.match(numSplt, patronsImg)   #Mira a quin nombre s'assembla
        matriculaNumbers.append(matriculaMatch)     #Afegeix el nombre de la matricula a la llista que conte tots els nombres de la matricula
        matriculaSplit = splt[1]    #Assigna la part de la imatge que ha sobrat al que s'haura de retallar a la seguent repeticio
        if (len(matriculaSplit[1]) == 0):   #Si la llargada es 0 voldra dir que no hi ha mes imatge per analitzar i se sortira del bucle
            break
    return matriculaNumbers

def hasLettersInMat():
    """
    Pregunta si la matricula te lletres, en cas afirmatiu, agafa 4 nombres
    """
    while True:
        lettersInMat = raw_input("La matricula te lletres?(Y/N) ")
        if(lettersInMat == "y" or lettersInMat == "Y"):
             return True
        elif(lettersInMat == "n" or lettersInMat == "N"):
            return False
        print lettersInMat + " no es una resposta valida."

def nombreMatricula(patrons, matricula):
    """
    Retorna una string que conte la matricula identificada
    """
    lettersInMat = hasLettersInMat()    #Demana si la matricula te lletres

    if (lettersInMat):
        print "Les matricules amb lletres solen tenir 4 nombres"

    patronsImg = getPatr(patrons)   #Obte patrons
    hPatrons = img.get_h(patronsImg[0]) #Obte alcada de patrons

    matriculaImg = getMatr(matricula, hPatrons) #Obte matricula

    matriculaNumberList = getMatriculaNumbers(matriculaImg, patronsImg, lettersInMat) #Obte una llista amb els nombres de la matricula
    matriculaNumberList = list(map(str, matriculaNumberList))  # Converteix la llista de int a llista de strings
    matStr = "".join(matriculaNumberList)   #Els ajunta en format string
    print "La matricula identificada es " + matStr  #Printeja la matricula identificada
    return matStr

if(__name__ =="__main__"):
    s = sys.argv[1:]
    patrons = s[0]
    matricula = s[1]

    nombreMatricula(patrons, matricula)



