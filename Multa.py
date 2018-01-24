


def consultarMultes(fitxer)
    f=open(fitxer)
    linia=f.readline()
    comptador=0
    while linia!="":
        c=linia.split("/")
        comptador+=1
        print "num",comptador,"num matricula->",c[0],"diners a pagar->",c[1]
    f.close()

def logIn():
    us="Agent1"
    pas="policia"
    usuari=input("entri usuari: ")
    password=input("entri contrasenya")
    success=False
    while usuari!=us and password!=pas:
        success=False
        usuari=input("entri usuari: ")
        password=input("entri contrasenya")
    return True
