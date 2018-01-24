import img2char, os.path, Multa

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
        if(Multa.checkIfInt(fee)):
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



