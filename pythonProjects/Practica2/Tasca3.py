import mainLib, itertools, random
minLength = 1
maxLength = 9

def AskWord():
    """
    Retorna l'input que l'usuari introdueix
    Per que es pugui retornar la paraula ha de ser alfabetica, totes les lletres minuscules
    i la llargada ha d'estar entre la llargada minima i la maxima
    """
    correctWord = False
    while not correctWord:
        word = mainLib.askWord()
        if (minLength <= len(word) <= maxLength):
            correctWord = True
        else:
            print "The word must be between", minLength, "and", maxLength, "characters"
    return word

def getRandomPermutation(permutations):
    """
    Et retorna una permutacio aleatoria de les que hi ha a la llista que l'hi passes
    """
    return permutations[random.randint(0, len(permutations) - 1)]

def Tasca3():
    """
    A partir d'una paraula que introdueix l'usuari crea totes les permutacions possibles
    En selecciona una d'aleatoria i va probant una per una aviam si la troba
    Un cop la troba et diu que l'ha trobat i amb quants intents ho ha fet
    """
    permutations = list(itertools.permutations(AskWord()))
    discover = getRandomPermutation(permutations)
    print "Generation of random code done"
    intents = 0
    print "Starting to decode..."
    for e in permutations:
        intents += 1
        if (e == discover):
            print "Success"
            print "Combination guessed ecirpo at opportunity:", intents
            break
