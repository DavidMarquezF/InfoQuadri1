import mainLib, string, time
from getpass import getpass

def chequejaParaula (p):
    """
    Chequeja si la paraula es alfabetica i nomes conte minuscules
    >>> chequejaParaula('')
    False
    >>> chequejaParaula('inf0rmatica')
    False
    >>> chequejaParaula('info12be')
    False
    >>> chequejaParaula('nose@e')
    False
    >>> chequejaParaula('aa')
    True
    >>> chequejaParaula('A')
    False
    """
    if len(p) == 0:
        return False
    for c in p:
        if(c not in string.lowercase):
            return False
    return True


def Intro():
    """
    Es la funcio que inicialitza aquest joc, preguntant si la persona vol jugar o no
    """
    print "Welcome to the game HangMan!"
    if (mainLib.askYorNQuestion("Are you ready to begin? ")):
        print
        print
        StartGame()

def Player2():
    """
    Pregunta al jugador 2 (l'alcalde) una paraula per que endevini el jugador 1 (acusat)
    """
    print "The mayor is the person who has to create the word"
    print "What word do you want the accused to guess?"
    gotWord = False
    while not gotWord:
        word = getpass("--> ")
        if (chequejaParaula(word)):
            gotWord = True
        else:
            print "Bad word including not lower alphabetical letters"
    return word

def StartGame():
    """
    Fa anar tot el joc (pregunta la paraula, fa que jugui l'acusat, etc.)
    """
    print "You are an innocent person that"
    print "faces trial for something you haven't done"
    print "You can do only 1 thing to survive: "
    print "Guess the RIGHT WORD"
    time.sleep(2)
    print
    print

    secret = Player2()
    print "The challenge begins!"
    oportunitats = 11
    oculta = "@"*len(secret)
    i = 0
    success = False
    lettersUsed = ""
    print "This is the hidden word: ", oculta
    while i < oportunitats and not success:
        lletra = raw_input("Enter a letter: ")
        while lletra not in string.lowercase or len(lletra) != 1 or lletra in lettersUsed:
            if(lletra in lettersUsed):
                print "You have already used this letter! The letters you have used are:"
                for e in lettersUsed:
                    print e.upper()+ ", ",
                print
            lletra = raw_input("Enter correct letter: ")

        lettersUsed += lletra
        if(lletra in secret):
            oculta = mainLib.endevinantParaula(secret, oculta, lletra)
            print "You were right!"
        else:
            i += 1
            print "You are wrong"
            print
            Graphics(i)
        if(oculta == secret):
            success = True
            print "You have guessed the word correctly!"
            print "You are free to go."
        elif(i < oportunitats):
            print "The word as it is: ", oculta
    print "The correct word was:", secret

def Graphics(intent):
    """
    Controla els grafics del penjat
    """
    if(intent == 0):
        print "You havent missed yet!"
    elif(intent == 1):
        print
        print
        print
        print
        print "___________"
    elif (intent == 2):
        print"|"
        print"|"
        print"|"
        print"|"
        print"|__________"
    elif (intent == 3):
        print "________"
        print"|"
        print"|"
        print"|"
        print"|"
        print"|__________"
    elif (intent == 4):
        print "________"
        print"|/"
        print"|"
        print"|"
        print"|"
        print"|__________"
    elif (intent == 5):
        print "________"
        print"|/       |"
        print"|"
        print"|"
        print"|"
        print"|__________"
    elif (intent == 6):
        print "________"
        print"|/       |"
        print"|        0"
        print"|"
        print"|"
        print"|__________"
    elif (intent == 7):
        print "________"
        print"|/       |"
        print"|        0"
        print"|        |"
        print"|"
        print"|__________"
    elif (intent == 8):
        print "________"
        print"|/       |"
        print"|        0"
        print"|       /|"
        print"|"
        print"|__________"
    elif (intent == 9):
        print "________"
        print"|/       |"
        print"|        0"
        print"|       /|\ "
        print"|"
        print"|__________"
    elif (intent == 10):
        print "________"
        print"|/       |"
        print"|        0"
        print"|       /|\ "
        print"|       /"
        print"|__________"
    else:
        print "________"
        print"|/       |"
        print"|        0"
        print"|       /|\ "
        print"|       / \ "
        print"|__________"
        print "You have lost the challenge!"
        print "You are HANG!"
        print "GAME OVER"

    print




