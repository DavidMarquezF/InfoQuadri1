


def consultarMultes(fitxer)
    fitxer=sys.argv[1]
    f=open(fitxer)
    linia=f.readline()
    while linia!="":
        c=linia.split(-)
        print "n->",c[0],"num matricula->",c[1],"diners a pagar",c[2]
    f.close()

def logIn():
    us=Agent1
    pas=policia
    usuari=imput("entri usuari: ")
    password=input("entri contrasenya")
    success=False
    while usuari!=us and password!=pas:
        success=False
        usuari=imput("entri usuari: ")
        password=input("entri contrasenya")

    if success=True:
        menuOpcions()