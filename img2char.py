import sys, discret, img, imgio,match,split,transf

def getPatr(patrons):
    patronsImg = match.load_patterns(patrons)
    for i, patro in enumerate(patronsImg):
        patronsImg[i] = discret.rgb_to_bn(patro)
    return patronsImg

def getMatr(matricula, hPatrons):
    matriculaImg = imgio.read_rgb(matricula)
    matriculaImg = discret.rgb_to_bn(matriculaImg)
    matriculaImg = transf.vtrim(matriculaImg)
    matriculaImg = transf.scale(matriculaImg, hPatrons)

    return  matriculaImg


def getMatriculaNumbers(matriculaImg, patronsImg, hasLetters = False):
    matriculaNumbers = []
    matriculaSplit = matriculaImg

    i = 0
    while True:
        if(hasLetters):
            i+=1
            if(i > 4):
                break

        splt = split.split_digit(matriculaSplit)
        if (splt == img.null()):
            break
        numSplt = transf.htrim(splt[0])
        matriculaMatch = match.match(numSplt, patronsImg)
        matriculaNumbers.append(matriculaMatch)
        matriculaSplit = splt[1]
        if (len(matriculaSplit[1]) == 0):
            break
    return matriculaNumbers

def hasLettersInMat():
    while True:
        lettersInMat = raw_input("La matricula te lletres?(Y/N) ")
        if(lettersInMat == "y" or lettersInMat == "Y"):
            lettersInMat = True
            break
        elif(lettersInMat == "n" or lettersInMat == "N"):
            lettersInMat = False
            break
        print lettersInMat + " no es una resposta valida."


if(__name__ =="__main__"):
    s = sys.argv[1:]
    patrons = s[0]
    matricula = s[1]
    lettersInMat = hasLettersInMat()

    if(lettersInMat):
        print "Les matricules amb lletres solen tenir 4 nombres"

    patronsImg = getPatr(patrons)
    hPatrons = img.get_h(patronsImg[0])

    matriculaImg = getMatr(matricula, hPatrons)

    print getMatriculaNumbers(matriculaImg,patronsImg, lettersInMat)


