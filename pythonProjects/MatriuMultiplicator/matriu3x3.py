import mainLib
maxFilesiCol = 6
minFilesiCol = 2

def opcions():
    """
    Printeja les opcions que es poden solucionar
    """
    print "[1] Llegir matriu A"
    print "[2] Llegir matriu B"
    print "[3] Calcular A + B"
    print "[4] Calcular A - B"
    print "[5] Calcular A * B"
    print "[6] Calcular determinant"
    print "[7] Calcular trasposada"
    print "[8] Sortir"


def AdministrarCrearMatriu(lletra):
    """
    S'ocupa de la creacio de matrius (ja sigui per la matriu A o la B)
    """
    print "Creacio de matriu " + lletra.upper() + ": "
    x = mainLib.creaMatriu(mainLib.demanarFilesColumnes("f", minFilesiCol, maxFilesiCol), mainLib.demanarFilesColumnes("c", minFilesiCol, maxFilesiCol))
    print
    print "Matriu "+ lletra.upper() + ": "
    mainLib.mostraMatriu(x)
    return x

def AdministrarOperacio(operacio, a, b):
    """
    S'ocupa de fer totes les operacions que involucren a les dos matrius (multiplicacio, suma i resta)
    """
    if(mainLib.checkIfCanOperate(a, b)):
        if(operacio == "+"):
            op = "Suma"
            x = mainLib.sumaMatrius(a, b)
        elif(operacio == "-"):
            op = "Resta"
            x = mainLib.restaMatrius(a, b)
        else:
            op = "Multiplicacio"
            x = mainLib.multMatrius(a, b)

        print op + " de A i B: "
        print
        mainLib.mostraMatriu(a)
        print "  " + operacio
        mainLib.mostraMatriu(b)
        print "  ||"
        mainLib.mostraMatriu(x)

    else:
        print mainLib.whichMatrixIsEmpty(a, b)

def OperacioUnaMatriu(operacio,m, nomMatriu):
    """
    Fa l'operacio d'una matriu dessitjada sobre la matriu seleccionada (m)
    """
    if (len(m) != 0):
        if (operacio == "d"):
            if(mainLib.verificaMatriuQuadrada(m)):
                print "Determinant de",nomMatriu,":"
                print mainLib.detMatriu(m, 1)
            else:
                print "La matriu", nomMatriu, "no es quadrada"
        else:
            print "Trasposada de", nomMatriu,":"
            mainLib.mostraMatriu(mainLib.trasposada(m))
    else:
        print "Matriu", nomMatriu, "es buida"


def AdministrarOperacioUnaMatriu(operacio, a, b):
    """
    S'ocupa de les operacions de una matriu (et fa triar sobre quina vols fer l'operacio i la hi fa)
    """
    if(operacio == "d"):
        op = "Determinant"
    else:
        op = "Trasposada"

    aOrB = mainLib.askNumberOption(op +" de A (1) o de B (2): ", 2)
    if (aOrB == 1):
        OperacioUnaMatriu(operacio, a, "A")
    else:
        OperacioUnaMatriu(operacio, b, "B")


def operar():
    """
    Es la funcio principal del programa.
    S'ocupa de mostrar el menu i cridar les funcions necessaries per a fer l'opcio seleccionada
    """
    a=[]
    b = []
    exit =False
    while not exit:
        print
        opcions()
        op = mainLib.askNumberOption("Choose an option: ", 8)
        print
        if(op == 1):
            a = AdministrarCrearMatriu("a")
        elif(op == 2):
            b = AdministrarCrearMatriu("b")
        elif (op == 3):
            AdministrarOperacio("+",a,b)
        elif(op == 4):
            AdministrarOperacio("-", a, b)
        elif (op == 5):
            AdministrarOperacio("*", a, b)
        elif(op == 6):
            AdministrarOperacioUnaMatriu("d",a,b)
        elif(op == 7):
            AdministrarOperacioUnaMatriu("t",a,b)
        else:
            exit = True

if(__name__ == "__main__"):
    operar()