import img
def split_digit(imag):
    """
    Reotrna una tupla amb la imatge del primer nombre retallat seguida de la resta de la imatge
    >>> split_digit(("1", [[255,255,0,255,255,0,0,0,255],[255,0,0,255,255,255,255,255,255],[255,255,0,255,255,0,0,0,255],[255,255,0,255,255,0,0,0,255]]))
    (('1', [[255, 0], [0, 0], [255, 0], [255, 0]]), ('1', [[255, 255, 0, 0, 0, 255], [255, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 255], [255, 255, 0, 0, 0, 255]]))
    """
    matrix  = img.matrix(imag)
    if (img.format(img.img(matrix)) != "1"): #Nomes pot ser blanci negre
        raise Exception("The format must be black and white")

    start = findBlack(matrix)   #Troba on comenca el nombre (columna de pixels negres)
    if(start == None):          #Si no es troba pixels negres es retornara una imatge nula, ja que no hi ha cap mes nombre per retallar
        return img.null()

    finish = findWhite(matrix, start)   #Troba on acaba el nombre, es a dir a la columna abans d'on nomes hi ha una columna blanca

    croppedNumber = img.subimg(imag,start, 0, finish -start, len(matrix))  #Retalla el nombre --> Des don comenca el nombre, amb l'amplada que te  = Final - comencament
    endCropped = img.subimg(imag, finish+1, 0, len(matrix[0]) - finish+1, len(matrix))  #La resta del nombre
    return (croppedNumber, endCropped)  #Retorna la tupla  amb el nombre retallat i la  resta


def findBlack(matrix):
    """
    Troba una columna negre
    >>> findBlack([[255,0,0],[255,255,0]])
    1
    """
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
           if(matrix[row][col] != 255): #Si no es blanc sera negre per tant retornar que ha trobat columna negre
               return col
    return None #No hauria d'arribar aqui

def findWhite(matrix, startBlack):
    """
    Troba columna blanca despres de la columna negra i retorna la columna abans d'aquesta
    >>> findWhite([[255,0,255],[255,255,255]],1)
    1
    """
    neededWhite = len(matrix)   #El nombre de pixels blancs que hi ha d'haver en una columna totalment blanca es el nombre de files
    for col in range(startBlack, len(matrix[0])):   #Passara per totes les columnes des d'on s'ha trobat un pixel negre fins al final de la imatge si fa falta
        whites = 0  #Contador de pixels blancs
        for row in range(len(matrix)):
           if(matrix[row][col] == 255): #Si pixel es blanc es sumara
               whites += 1
        if(whites >= neededWhite):  #Si hi ha suficients pixels blancs (tota una columna blanca), retornara la columna anterior que sera on hi havien els ultims pixels negres
            return col-1 #La columna d'abans es la que encara tenia negre

    return None #No hauria d'arribar aqui
