import imgio, img
def getNames(prefix):
    i = 0
    names=[]
    while(i<=9):
        name = prefix + "_"+str(i)+".jpeg"
        names.append(name)
        i+=1
    return names

def load_patterns(prefix):
    names = getNames(prefix)
    images = []
    for name in names:
        images.append(imgio.read_rgb(name))
    return  images

def match(imag, patlst):
    #TODO: La imatge ha de ser la mateixa altura. Es fa aqui o es fa quan mho passen?
    #TODO: Em passen la imatge en blanc i negre?

    closestPattern = -1
    patternSim = 0
    for pat in range(len(patlst)):
        patSim = simImage(imag, patlst[pat])
        if(patSim > patternSim):
            patternSim = patSim
            closestPattern = pat

    return closestPattern




def simImage(imag, imag2):
    widthImg = img.get_w(imag)
    widthImg2 = img.get_w(imag2)
    if(widthImg == widthImg2):
        return sim(imag, imag2)
    else:
        diference = abs(widthImg2-widthImg)
        if(widthImg > widthImg2):
            return simBiggerImage(imag,imag2, widthImg2, diference)
        elif(widthImg2 > widthImg):
            return simBiggerImage(imag, imag2, widthImg, diference)

def simBiggerImage(smallImag, bigImag, smallestWidth, difference):
    """
    En cas que una imatge sigui mes grossa que l'altre es gestiona la semblanca aqui
    >>> simBiggerImage(('1', [[255,0,255],[255,0,255],[255,0,255]]),('1',[[255,255,0,255,255,255],[255,0,255,255,255,255],[0,255,255,255,255,255]]), 3, 3)
    6
    """
    biggestSim = 0
    for i in range(difference + 1):
        currentSim = sim(smallImag, bigImag, i)
        if (currentSim > biggestSim):
            biggestSim = currentSim
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
    compareWhitem1 = 255
    if(img.format(smallImag) == "RGB"):
        compareWhitem1 = (255,255,255)

    compareWhitem2 = 255
    if (img.format(bigImag) == "RGB"):
        compareWhitem2 = (255, 255, 255)

    m1 = img.matrix(smallImag)
    m2 = img.matrix(bigImag)


    samePixels = 0
    for row in range(len(m1)):
        for col in range(len(m1[0])):
            if(m1[row][col] == compareWhitem1 and m2[row][col+start] == compareWhitem2):
                samePixels+=1
            elif(m1[row][col] != compareWhitem1 and m2[row][col+start] != compareWhitem2):
                samePixels+=1
    return samePixels







