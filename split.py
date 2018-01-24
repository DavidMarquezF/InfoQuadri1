import img
def split_digit(imag):
    """
    >>> split_digit(("1", [[255,255,0,255,255,0,0,0,255],[255,0,0,255,255,255,255,255,255],[255,255,0,255,255,0,0,0,255],[255,255,0,255,255,0,0,0,255]]))
    (('1', [[255, 0], [0, 0], [255, 0], [255, 0]]), ('1', [[255, 255, 0, 0, 0, 255], [255, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 255], [255, 255, 0, 0, 0, 255]]))
    """
    matrix  = img.matrix(imag)
    if (img.format(img.img(matrix)) != "1"): #Nomes pot ser blanci negre
        raise Exception("The format must be black and white")

    start = findBlack(matrix)
    if(start == None):
        return img.null()
    finish = findWhite(matrix, start)
    croppedNumber = img.subimg(imag,start, 0, finish, len(matrix))
    endCropped = img.subimg(imag, finish+1, 0, len(matrix[0]) - (finish+1), len(matrix))
    return (croppedNumber, endCropped)


def findBlack(matrix):
    """
    Troba una columna negre
    >>> findBlack([[255,0,0],[255,255,0]])
    1
    """
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
           if(matrix[row][col] != 255):
               return col
    return None #No hauria d'arribar aqui

def findWhite(matrix, startBlack):
    """
    Troba columna blanca despres de la columna negra i retorna la columna abans d'aquesta
    >>> findWhite([[255,0,255],[255,255,255]],1)
    1
    """
    neededWhite = len(matrix)
    for col in range(startBlack, len(matrix[0])):
        whites = 0
        for row in range(len(matrix)):
           if(matrix[row][col] == 255):
               whites += 1
        if(whites >= neededWhite):
            return col-1 #La columna d'abans es la que encara tenia negre

    return None #No hauria d'arribar aqui
