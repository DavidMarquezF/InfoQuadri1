import img2char, os.path

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

