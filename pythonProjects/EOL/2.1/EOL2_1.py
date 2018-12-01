def escriu_opcions():
    print "1. Amanida vegetal"
    print "2. Pasta amb salsa bolonyesa"
    print "3. Plat especial del dia"
def opcions_amanida():
    print "a. Amb olives"
    print "b. Sense olives"
    print "c. Tornar al menu principal"

def amanida():
    while True:
        opcions_amanida()
        answer = raw_input("Introdueixi la seva tria: ")
        if(answer == "a"):
            return "amb olives"
        elif (answer == "b"):
            return "sense olives"
        elif(answer == "c"):
            return "back"
        else:
            print "Opcio incorrecte!"

def tria():
    finish = False
    while(not finish):
        escriu_opcions()
        num =input("Introdueixi la seva tria: ")
        if(num == 1):
            opcio = amanida()
            if(opcio != "back"):
                print  "Amanida vegetal " + amanida() + " a punt!"
        elif(num == 2):
            print "Pasta amb salsa bolonyesa a punt!"
        elif(num == 3):
            print "Plat especial del dia a punt!"
        elif(num == 4):
            print "Gracies per haver fet servir el programa de menus"
            finish = True
        else:
            print "Opcio incorrecta"

if __name__ == '__main__':

    tria()
