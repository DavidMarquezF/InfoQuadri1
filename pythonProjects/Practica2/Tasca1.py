import mainLib, string
llargadaMin =1
llargadaMax = 10


    
def LenParaula():
    """
    demana a l'usuari la longitud de la paraula que vol(de llargada entre 1 i 10) i te la retorna
    """
    longitud=raw_input("Enter len of the word you want to guess: ")
    
    while not mainLib.checkIfInt(longitud) or not llargadaMin<=int(longitud)<=llargadaMax:
        print "Not correct len. Enter a number between", llargadaMin,"and",llargadaMax
        longitud=raw_input("Enter len of the word you want to guess: ")
    
    longitud=int(longitud)
    print "Generated random code of len",longitud
    return longitud



def codiRandom():
    """
    retorna un condi random de lletres minuscules de la longitud que has introduit a la funcio LenParaula
    """
    cR=""
    i=0
    l=LenParaula()
    while i<l:
        cR+=mainLib.randomChoiceString(string.lowercase)
        i+=1
    return cR


def Tasca1():
    """
    Aqui a partir del codi aleatori creat i de la longitud seleccionada has d'endevinar els caracters del codi tenint com a intents la longitud de la parula. Si l'encertes has guanyat i sino has perdut
    """
    paraula=codiRandom()
    s="@"
    oculta=s*len(paraula)
    print "This is the word",oculta
    oportunitats=len(paraula)
    t=False
    i=0
    while i<oportunitats and not t:
        lletra = raw_input("Enter a letter: ")

        while lletra not in string.lowercase or len(lletra) != 1:
            lletra = raw_input("Enter correct letter: ")

        oculta=mainLib.endevinantParaula(paraula,oculta,lletra)
        if (oportunitats - i - 1 != 0):
            print "This is the word",oculta
            print "Remain",oportunitats-i-1,"opportunities"
        i+=1
        if oculta==paraula:
            t=True
    if t: 
        print "Congratulations. You win!!! The random code was -->",oculta
    else:
        print "Opps. The random code was -->",paraula

