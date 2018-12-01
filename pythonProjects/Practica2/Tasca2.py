import string, mainLib


def randomLetter(lettersUsed):
    """
    Retorna una lletra que no s'ha fet servir previament
    """
    success = False
    while not success:
        l = mainLib.randomChoiceString(string.lowercase)
        if(l not in lettersUsed):
            success = True
    return l




def decodeWord(word):
    """
    Descodifica la paraula que s'ha escollit
    Quan acaba de descifrar-la et printeja quants passos ha necessitat per fer-ho
    """
    lused = ""
    hidden = "@"*len(word)
    steps = 0
    while hidden != word:
        l = randomLetter(lused)
        lused += l
        print "Random letter",l
        hidden = mainLib.endevinantParaula(word, hidden,l)
        steps += 1
    print "End of deciphering", steps, "steps needed"

def Tasca2():
    """
    Funcio que es crida per fer portar a terme la Tasca 2
    """
    decodeWord(mainLib.askWord())

