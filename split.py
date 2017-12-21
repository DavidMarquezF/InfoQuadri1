import img, transf
def split_digit(imag):
    """
    >>> split_digit(("1", [[255,255,0,255,255,0,0,0,255],[255,0,0,255,255,255,255,255,255],[255,255,0,255,255,0,0,0,255],[255,255,0,255,255,0,0,0,255]]))
    (('1', [[255, 0], [0, 0], [255, 0], [255, 0]]), ('1', [[255, 255, 0, 0, 0, 255], [255, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 255], [255, 255, 0, 0, 0, 255]]))
    """
    matrix  = img.matrix(imag)
    if (img.format(img.img(matrix)) == "RGB" or img.format(img.img(matrix)) == "L"): #Nomes pot ser blanci negre
        raise Exception("The format must be black and white")

    start = findBlack(matrix)
    finish = findWhite(matrix, start)
    croppedNumber = img.subimg(imag,start, 0, finish, len(matrix))
    endCropped = img.subimg(imag, finish+1, 0, len(matrix[0]) - finish+1, len(matrix))
    return (croppedNumber, endCropped)


def findBlack(matrix):
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
           if(matrix[row][col] != 255):
               return col
    return None #No hauria d'arribar aqui

def findWhite(matrix, startBlack):
    neededWhite = len(matrix)
    for col in range(startBlack, len(matrix[0])):
        whites = 0
        for row in range(len(matrix)):
           if(matrix[row][col] == 255):
               whites += 1
        if(whites >= neededWhite):
            return col-1 #La columna d'abans es la que encara tenia negre

    return None #No hauria d'arribar aqui
