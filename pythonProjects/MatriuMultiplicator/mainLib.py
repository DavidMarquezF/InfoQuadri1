def checkIfInt(number):
    """
    Chequeja si la string que es passa es un int
    >>> checkIfInt('10')
    True
    >>> checkIfInt('1A')
    False
    >>> checkIfInt('asd')
    False
    """

    try:                #Prova de fer aixo
        int(number)
        return True
    except ValueError:  #Si dona error retorna False
        return False

#---------------------------------------------VERIFICACIO------

def checkIfCanOperate(a,b):
    """
    Mira si les matrius son buides
    >>> checkIfCanOperate([], [[0]])
    False
    >>> checkIfCanOperate([[0]], [[0]])
    True
    >>> checkIfCanOperate([[0]], [])
    False

    """
    return len(a) != 0 and len(b) != 0

def verificaSumaRestaPossible(a,b):
    """
    Mira si les matrius a i b es poden sumar o restar (el nombre de files i columnes ha de ser el mateix)
    >>> verificaSumaRestaPossible( [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    True
    >>> verificaSumaRestaPossible( [[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    False
    >>> verificaSumaRestaPossible( [[0, 0], [0, 0], [0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    False
    """
    return  len(a) == len(b) and len(a[0]) == len(b[0])

def verificaMultPossible(a,b):
    """
    Mira si es podra multiplicar (mateix nombre de columnes de la primera que files de la segona)
    >>> verificaMultPossible( [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    True
    >>> verificaMultPossible( [[0, 0, 0]], [[0, 0], [0, 0], [0, 0]])
    True
    >>> verificaMultPossible( [[0, 0], [0, 0], [0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    False
    """
    return len(a[0]) == len(b)
def verificaMatriuQuadrada(m):
    """
    Retorna True si la matriu es quadrada i False si no ho es
    >>> verificaMatriuQuadrada([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    True
    >>> verificaMatriuQuadrada([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    True
    >>> verificaMatriuQuadrada([[0, 0], [0, 0], [0, 0]])
    False
    >>> verificaMatriuQuadrada([[0, 0, 0], [0, 0, 0]])
    False
    """
    return len(m) == len (m[0])

def whichMatrixIsEmpty(a,b):
    """
    Retorna una string que diu quines matrius estan buides
    >>> whichMatrixIsEmpty([], [[0]])
    'La matriu A esta buida'
    >>> whichMatrixIsEmpty([], [])
    'Les matrius A i B estan buides'
    >>> whichMatrixIsEmpty([[0]], [])
    'La matriu B esta buida'
    """
    if(len(a) == 0 and len(b) == 0):
        return "Les matrius A i B estan buides"
    elif(len(a) == 0):
        return "La matriu A esta buida"
    else:
        return "La matriu B esta buida"


#---------------------------------------------DEMANAR A L'USUARI------

def askNumberOption(question, numbers):
    """
    Demana una pregunta (parametre 1) on es poden triar opcions del 1 al parametre 2 (numbers)
    i retorna el que l'usuari ha triat
    """
    while(True):
        answerUser = raw_input(question)
        while(not checkIfInt(answerUser)):
            answerUser = raw_input("Write a valid answer: ")
        answerUser = int(answerUser)
        if(answerUser > 0 and answerUser <= numbers):
            return answerUser


def askNumber(fila, col):
    """
    Demana el nombre per una posicio
    """
    success = False
    while not success:
        x = raw_input("Entra un nombre per la fila " +  str(fila) + ", columna " + str(col)+ ": ")
        success = checkIfInt(x)
        if(not success):
            print "Introdueix un nombre valid"
    return int(x)

def demanarFilesColumnes(foc, minFilesiCol, maxFilesiCol):
    """
    Demana les files o columnes que l'usuari voldra per crear una matriu
    """
    success = False
    if(foc == "f"):
        c = "files"
    else:
        c = "columnes"
    while not success:
        x = raw_input("Introueix quantes " + c + " vols (entre " +str(minFilesiCol) + " i " + str(maxFilesiCol)+"): " )
        if(checkIfInt(x) and minFilesiCol <= int(x) <= maxFilesiCol):
            success = True
        else:
            print "Has d'introduir un nombre enter entre", minFilesiCol, "i", maxFilesiCol
    return int(x)



#---------------------------------------------INICIALITZACIO I MOSTRAR MATRIUS------
def creaMatriu(files, columnes):
    """
    Crea una matriu de les files i columnes introduides en els parametres
    a partir del que l'usuari introdueix
    """
    m = []
    for i in range(files):
        fila = []
        for j in range(columnes):
            fila += [askNumber(i, j)]
        m+=[fila]
    return  m

def inicialitzaMatriu(f,c):
    """
    Creara una matriu buida
    >>> inicialitzaMatriu(3,3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> inicialitzaMatriu(4,3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> inicialitzaMatriu(3,4)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    m = []
    for i in range(f):
        fila = []
        for j in range(c):
            fila +=[0]
        m+=[fila]
    return  m

def mostraMatriu(m):
    """
    Mostra la matriu m
    """
    if (len(m) != 0):
        for fila in m:
            for columna in fila:
                print columna,
            print

#---------------------------------------------OPERACIONS AMB MATRIUS------
def sumaMatrius(a,b):
    """
    Suma matrius
    >>> sumaMatrius([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    >>> sumaMatrius([[2, 89, 9], [-1, 1, 22], [12, 3, 1]], [[7, 8, 9], [0, 0, -9], [-12, 2, -1]])
    [[9, 97, 18], [-1, 1, 13], [0, 5, 0]]
    >>> sumaMatrius([[2, 89, 9], [-1, 1, 22], [12, 3, 1]], [[0, 0, -9], [-12, 2, -1]])
    Les dues matrius no tenen el mateix nombre de files i columnes
    ['X']
    """
    if (not verificaSumaRestaPossible(a, b)):
        print "Les dues matrius no tenen el mateix nombre de files i columnes"
        return["X"]

    m=inicialitzaMatriu(len(a),len(a[0]))
    for i in range(len(a)):
        for j in range(len(a[0])):
            m[i][j]=a[i][j]+ b[i][j]
    return m

def restaMatrius(a,b):
    """
    Resta matrius
    >>> restaMatrius([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    >>> restaMatrius([[2, 89, 9], [-1, 1, 22], [12, 3, 1]], [[7, 8, 9], [0, 0, -9], [-12, 2, -1]])
    [[-5, 81, 0], [-1, 1, 31], [24, 1, 2]]
    >>> restaMatrius([[2, 89, 9], [-1, 1, 22], [12, 3, 1]], [[0, 0, -9], [-12, 2, -1]])
    Les dues matrius no tenen el mateix nombre de files i columnes
    ['X']
    """
    if (not verificaSumaRestaPossible(a, b)):
        print "Les dues matrius no tenen el mateix nombre de files i columnes"
        return["X"]

    m=inicialitzaMatriu(len(a),len(a[0]))
    for i in range(len(a)):
        for j in range(len(a[0])):
            m[i][j]=a[i][j]- b[i][j]
    return m

def multMatrius(a,b):
    """
    Multiplicacio matrius
    >>> multMatrius([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> multMatrius([[2, 89, 9], [-1, 1, 22], [12, 3, 1]], [[7, 8, 9], [0, 0, -9], [-12, 2, -1]])
    [[-94, 34, -792], [-271, 36, -40], [72, 98, 80]]
    >>> multMatrius([[1, 3, 5, 7], [2, 4, 6, 8]], [[1, 8, 9], [2, 7, 10], [3, 6, 11], [4, 5, 12]])
    [[50, 94, 178], [60, 120, 220]]
    >>> multMatrius([[2, 89, 9], [-1, 1, 22]], [[7, 8, 9], [-12, 2, -1]])
    La matriu A ha de tenir el mateix nombre de columnes que les files que te la matriu B
    ['X']
    """
    if(not verificaMultPossible(a,b)):
        print "La matriu A ha de tenir el mateix nombre de columnes que les files que te la matriu B"
        return ["X"]

    m = inicialitzaMatriu(len(a),len(b[0]))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                m[i][j] += a[i][k] * b[k][j]
    return m

def detMatriu(m, mul):
    """
    Calcula el determinant de qualsevol matriu quadrada
    >>> detMatriu([[3, 8], [4, 6]], 1)
    -14
    >>> detMatriu([[6, 1, 1], [4, -2, 5], [2, 8, 7]], 1)
    -306
    >>> detMatriu([[1, 5, 4, 2], [-2, 3, 6, 4], [5, 1, 0, -1], [2, 3, -4, 0]], 1)
    242
    """
    f = len(m)
    if(f == 1):
        return mul * m[0][0]
    else:
        total = 0
        signe = -1

        for i in range(f):
            n = []
            for j in range(1,f):
                fila = []
                for k in range(f):
                    if(k != i):
                        fila += [m[j][k]]
                n += [fila]
            signe *= -1
            total += mul * detMatriu(n, signe * m[0][i])
        return  total

def trasposada(m):
    """
    Crea la trasposada de la matriu que se li passa
    >>> trasposada([[1,2,3],[4,5,6],[7,8,9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    >>> trasposada([[1,2],[4,5],[7,8]])
    [[1, 4, 7], [2, 5, 8]]
    """
    files = len(m)
    columnes = len(m[0])
    n = inicialitzaMatriu(columnes,files)
    for i in range(files):
        for j in range(columnes):
            n[j][i] = m[i][j]
    return n



