import sys, discret, img, imgio,match,split,transf

def getPatr(patrons):
    """
    Obte tots els patrons en blanc i negre
    """
    patronsImg = match.load_patterns(patrons)
    for i, patro in enumerate(patronsImg):
        patronsImg[i] = discret.rgb_to_bn(patro)
    return patronsImg

def getMatr(matricula, hPatrons):
    """
    Obte la matricula, la passa a blanc i negre, la retalla verticalment i l'escala
    """
    matriculaImg = imgio.read_rgb(matricula)
    matriculaImg = discret.rgb_to_bn(matriculaImg)
    matriculaImg = transf.vtrim(matriculaImg)
    matriculaImg = transf.scale(matriculaImg, hPatrons)

    return  matriculaImg


def getMatriculaNumbers(matriculaImg, patronsImg, hasLetters = False):
    """
    Retorna una llista amb cada nombre de la matricula (fa split, match,etc.)
    """
    matriculaNumbers = []
    matriculaSplit = matriculaImg

    i = 0
    while True:
        if(hasLetters):
            i+=1
            if(i > 4):
                break

        splt = split.split_digit(matriculaSplit)
        if (img.is_null(splt)):
            break
        numSplt = transf.htrim(splt[0])
        matriculaMatch = match.match(numSplt, patronsImg)
        matriculaNumbers.append(matriculaMatch)
        matriculaSplit = splt[1]
        if (len(matriculaSplit[1]) == 0):
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
    lettersInMat = hasLettersInMat()

    if (lettersInMat):
        print "Les matricules amb lletres solen tenir 4 nombres"

    patronsImg = getPatr(patrons)
    hPatrons = img.get_h(patronsImg[0])

    matriculaImg = getMatr(matricula, hPatrons)

    matriculaNumberList = getMatriculaNumbers(matriculaImg, patronsImg, lettersInMat)
    matriculaNumberList = list(map(str, matriculaNumberList))  # Convertir a string
    matStr = "".join(matriculaNumberList)
    print "La matricula identificada es " + matStr
    return matStr

if(__name__ =="__main__"):
    s = sys.argv[1:]
    patrons = s[0]
    matricula = s[1]

    nombreMatricula(patrons, matricula)



