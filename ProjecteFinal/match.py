import imgio, img
def getNames(prefix):
    """
    Retorna una llista de noms a partir d'un prefix
    >>> getNames("patro")
    ['patro_0.jpeg', 'patro_1.jpeg', 'patro_2.jpeg', 'patro_3.jpeg', 'patro_4.jpeg', 'patro_5.jpeg', 'patro_6.jpeg', 'patro_7.jpeg', 'patro_8.jpeg', 'patro_9.jpeg']
    """

    i = 0
    names=[]
    while(i<=9):    #Nomes tindrem 9 patrons
        name = prefix + "_"+str(i)+".jpeg"  #El nom del patro
        names.append(name)
        i+=1
    return names

def load_patterns(carpeta):
    """
    Et retorna les imatges de tots els patrons (imatges del 0 al 9)
    """
    prefix = carpeta[carpeta.rfind("/") + 1:]   #Troba el prefix dels patrons buscant la ultima barra (rfind busca d'endarrere endavant)
    carpeta = carpeta[:carpeta.rfind("/") + 1]  #La carpeta sera tota la  resta
    names = getNames(prefix)    #Obtindra la llista de noms
    images = []
    for name in names:
        images.append(imgio.read_rgb(carpeta+name)) #Llegeix totes les imatges dels patrons
    return  images

def match(imag, patlst):
    """
    Returns the number the image is closest to
    >>> match(("1", [[255,255,0,255],[255,0,0,255],[255,255,0,255],[255,255,0,255]]),[("1", [[0,0,0],[0,255,0],[0,255,0],[0,0,0]]), ("1", [[255,0,255],[0,0,255],[255,0,255],[255,0,255]])])
    1
    """
    closestPattern = -1     #El nombre que s'assembla mes. S'inicialitza a menys 1 perque es un nombre que no tenim
    patternSim = 0          #El nombre de pixels en comu que te

    for pat in range(len(patlst)):  #Probara tots els patrons
        patSim = simImage(imag, patlst[pat])    #Retorna el nombre de pixels en comu

        if(patSim > patternSim):    #Si la similitud es mes gran que la similitud del ultim nombre amb major similitud
            patternSim = patSim     #S'assigna els pixels en comu
            closestPattern = pat    #S'assigna el patro a el patro amb mes similitud

    return closestPattern   #Retorna el nombre amb mes pixels iguals




def simImage(imag, imag2):
    """
    Retorna la similtud entre dos imatges (un nombre de pixels)
    >>> simImage(('1', [[255,0,255],[255,0,255],[255,0,255]]),('1',[[255,255,0,255,255,255],[255,0,255,255,255,255],[0,255,255,255,255,255]]))
    6
    >>> simImage(('1', [[255, 0], [255, 255], [255, 255]]),('1', [[255, 0], [255, 0], [255, 255]]))
    5
    >>> simImage(('1', [[255, 0], [255, 255], [255, 255]]),('RGB', [[(255,255,255), (0,0,0)], [(255,255,255), (0,0,0)], [(255,255,255), (255,255,255)]]))
    5
    """
    widthImg = img.get_w(imag)      #Amplada de la imatge 1 (nombre retallat)
    widthImg2 = img.get_w(imag2)    #Amplada de la imatge 2 (patro a comparar)
    if(widthImg == widthImg2):      #Si tenen la mateixa amplada
        return sim(imag, imag2)     #Retorna directament la similitud entre les imatges comparant els pixels
    else:                           #Si no tenen la mateixa amplada cal probar totes les combinacions i agafar la que te mes pixels en comu
        diference = abs(widthImg2-widthImg)     #La diferencia d'amplada
        if(widthImg > widthImg2):               #Si la imatge 1 es mes gran que la imatge 2 passara la 2 com a smallImag i la 1 com a bigImag
            return simBiggerImage(imag2,imag, diference)
        elif(widthImg2 > widthImg):             #Si la imatge 2 es mes gran que la imatge 1 passara la 1 com a smallImag i la 2 com a bigImag
            return simBiggerImage(imag, imag2, diference)

def simBiggerImage(smallImag, bigImag, difference):
    """
    En cas que una imatge sigui mes grossa que l'altre es gestiona la semblanca aqui
    >>> simBiggerImage(('1', [[255,0,255],[255,0,255],[255,0,255]]),('1',[[255,255,0,255,255,255],[255,0,255,255,255,255],[0,255,255,255,255,255]]), 3)
    6
    >>> simBiggerImage(('1', [[255,0,255],[255,0,255],[255,0,0]]),('1',[[255,255,0,255,255,255],[255,0,255,255,255,255],[0,255,255,255,255,255]]), 3)
    5
    """
    biggestSim = 0      #La semblanca mes gran trobada
    for i in range(difference + 1): #Proba totes les combinacions
        currentSim = sim(smallImag, bigImag, i) #La similitud posant la imatge petita, la imatge gran i el comencament de comparar a i (que anira incrementant fins que s'hagin trobat totes les possibilitats)
        if (currentSim > biggestSim):
            biggestSim = currentSim     #Si la similitud trobada es mes gran que la mes gran guardada es guarda
    return biggestSim


def sim(smallImag, bigImag, start = 0):
    """
    Retorna la similitud entre 2 imatges
    >>> sim(('1', [[255, 255], [255, 255], [255, 255]]),('1', [[255, 255], [255, 255], [255, 255]]))
    6
    >>> sim(('1', [[255, 0], [255, 255], [255, 255]]),('1', [[255, 0], [255, 0], [255, 255]]))
    5
    >>> sim(('1', [[255, 0], [255, 255], [255, 255]]),('RGB', [[(255,255,255), (0,0,0)], [(255,255,255), (0,0,0)], [(255,255,255), (255,255,255)]]))
    5
    >>> sim(('1', [[255, 0], [255, 255], [255, 255]]),('1', [[255, 0, 255], [255, 0, 255], [255, 255, 255]]),1)
    3
    >>> sim(('1', [[255, 0, 255], [255, 255, 255], [255, 255, 255]]),('1', [[255, 0, 255], [255, 0, 255], [255, 255, 255]]),0)
    8
    """
    compareWhitem1 = 255    #El pixel blanc
    if(img.format(smallImag) == "RGB"): #Si el format es RGB s'haura de comparar amb el pixel blanc en format RGB
        compareWhitem1 = (255,255,255)

    compareWhitem2 = 255    #S'aplica de la mateixa manera per la imatge 2
    if (img.format(bigImag) == "RGB"):
        compareWhitem2 = (255, 255, 255)

    m1 = img.matrix(smallImag)  # Agafa les matrius de les imatges
    m2 = img.matrix(bigImag)


    samePixels = 0  #Pixels iguals
    for row in range(len(m1)):
        for col in range(len(m1[0])):
            if(m1[row][col] == compareWhitem1 and m2[row][col+start] == compareWhitem2):    #Si el pixel es blanc a les dues imatges la similitud es suma 1 als pixels en comu
                samePixels+=1
            elif(m1[row][col] != compareWhitem1 and m2[row][col+start] != compareWhitem2):  #Si el pixel no es blanc en les dues (es a dir que es negre) tambe se suma 1
                samePixels+=1
    return samePixels







