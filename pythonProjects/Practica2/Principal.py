import mainLib
from Tasca1 import Tasca1
from Tasca2 import Tasca2
from Tasca3 import Tasca3
from Penjat import Intro


def Options():
    """
    Printeja la llista d'opcions que l'usuari pot triar
    """
    print "Choose an option:"
    print "[1] Decipher machine code"
    print "[2] Decipher user code"
    print "[3] Generate all combinations"
    print "[4] Play the hang man"
    print "[5] Exit"

def descipher():
    """
    Crida les funcions creades en les Tasques depenent del que usuari trii
    Si es tria l'opcio 4 (exit), s'acabara el programa
    """
    finish = False
    while not finish:
        Options()
        op = mainLib.askNumberOption("Enter correct option: ", 5)
        if (op == 1):
            Tasca1()
        elif (op == 2):
            Tasca2()
        elif (op == 3):
            Tasca3()
        elif (op == 4):
            Intro()
        else:
            finish = True

if(__name__ == "__main__"):
    descipher()

