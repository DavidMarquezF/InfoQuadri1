import img2char, os.path, Multa

#---------------------Afegir Multa
def askFile():
    while True:
        f = raw_input("Introdueixi el fitxer amb la imatge")
        if(os.path.isfile(f)):
            return f
        else:
            print f + " no es un fitxer"

def askFee():
    while True:
        fee = raw_input("Introdueixi la multa (en euros)")
        if(Multa.checkIfInt(fee)):
            print "Multa de " + fee + " sera afegida a la matricula"
            return int(fee)

def AfegirMulta(patr, dic):
    matr = askFile()
    matricula = img2char.nombreMatricula(patr, matr)
    multa = askFee()
    if(dic.has_key(matricula)):
        dic[matricula] += multa
    else:
        dic[matricula] = multa
    return dic

def dicToString(dic):
    listText = []
    for key in dic.keys():
        listText.append(key+"/"+dic[key]);
    return listText

def writeToFile(file, listTxt):
    f = open(file,"w")
    f.writelines(listTxt)
    f.close()



