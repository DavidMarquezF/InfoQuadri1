def null():
    """
    Return the null image (Type, Matrix) == ("Null",None)
    >>> null()
    ('NULL', None)
    """
    return ("NULL",None)

def is_null(i):
    """
    Check if an image (Type, Matrix) == ('NULL', None)
    >>> is_null(('NULL', None))
    True
    """
    return i == null()


def white(w,h):
    """
    Retorna una llista de w x h amb tot 255
    """
    m = []
    for i in range(h):
        fila = []
        for j in range(w):
            fila += [255]
        m += [fila]
    return m

def white_rgb(w,h):
    """
    Returns an image in RGB format with all white pixels w x h
    >>> white_rgb(3,3)
    ('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]])
    """
    m = []
    for i in range(h):
        fila = []
        for j in range(w):
            fila += [(255,255,255)]
        m += [fila]
    return ("RGB", m)


def white_grey(w, h):
    """
    Returns an image in grey format with all white pixels w x h
    >>> white_grey(3,3)
    ('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
    >>> white_grey(5,2)
    ('L', [[255, 255, 255, 255, 255], [255, 255, 255, 255, 255]])
    """
    return ("L", white(w, h))


def white_bn(w, h):
    """
    Returns an image in grey format with all white pixels w x h
    >>> white_bn(3,3)
    ('1', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
    >>> white_bn(5,2)
    ('1', [[255, 255, 255, 255, 255], [255, 255, 255, 255, 255]])
    """
    return ("1", white(w, h))

def format(img):
    """
    Returns the image format
    >>> format(('1', [[255, 255], [255, 255], [255, 255]]))
    '1'
    >>> format(('L', [[255, 255], [255, 255], [255, 255]]))
    'L'
    """
    return img[0]

def matrix(img):
    """
    Return the pixel matrix of the image
    >>> matrix(('1', [[255, 255], [255, 255], [255, 255]]))
    [[255, 255], [255, 255], [255, 255]]
    """
    return img[1]

def img(matrix, model = "DISCOVER"):        ## TODO: No entenc lo del model
    """
    Returns the image representation format (T, m)
    >>> img([[255,255,0],[255,128,255],[191,255,255]],'DISCOVER')
    ('L', [[255, 255, 0], [255, 128, 255], [191, 255, 255]])
    >>> img([[255,255,0],[255,0,255],[0,255,255]],'DISCOVER')
    ('1', [[255, 255, 0], [255, 0, 255], [0, 255, 255]])
    >>> img([[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]])
    ('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]])
    """
    if(type(matrix[0][0]) is tuple):
        return ("RGB", matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] != 0 and matrix[i][j] != 255):
                return ("L", matrix)

    return ("1", matrix)

def get_w(img):
    """
    Returns the image width
    >>> get_w(('1', [[255, 255], [255, 255], [255, 255]]))
    2
    >>> get_w(('1', [[255, 255,255, 255], [255, 255,255, 255], [255, 255,255, 255]]))
    4
    """
    return len(img[1][0])

def get_h(img):
    """
    Returns the image height
    >>> get_h(('1', [[255, 255], [255, 255], [255, 255]]))
    3
    >>> get_h(('1', [[255, 255], [255, 255], [255, 255],[255, 255]]))
    4
    """
    return len(img[1])

def cropImage(matrix, ow, oh):
    """
    Retalla l'imatge a partir dels origens donats
    >>> cropImage([[255, 255], [255, 255], [255, 255],[255, 255]], 0,0)
    [[255, 255], [255, 255], [255, 255], [255, 255]]
    >>> cropImage([[255, 14], [0, 255], [255, 0],[255, 255]],1,0)
    [[14], [255], [0], [255]]
    >>> cropImage([[255, 14], [0, 255], [255, 0],[255, 255]],0,1)
    [[0, 255], [255, 0], [255, 255]]
    """
    m = []
    for i in range(oh, len(matrix)):
        fila = []
        for j in range(ow, len(matrix[0])):
            fila.append(matrix[i][j])
        m.append(fila)
    return m

def subimg(img, ow, oh, w, h):
    """
    Returns a subimage from img with origin coordinates ow,oh and size w x h
    >>> subimg(('L', [[0, 0, 255], [255, 255, 255], [255, 255, 255]]),0,0,2,1)
    ('L', [[0, 0]])
    >>> subimg(('1', [[255, 255], [255, 255], [255, 255]]),0,1,2,1)
    ('1', [[255, 255]])
    >>> subimg(('1', [[255, 255], [255, 255], [0, 255]]),0,1,2,2)
    ('1', [[255, 255], [0, 255]])
    """
    imgh = get_h(img)
    imgw = get_w(img)

    if(ow > imgw):
        return null()
    if(oh > imgh):
        return null()

    form = format(img)
    ma = cropImage(matrix(img), ow, oh)
    newImg = (form, ma)
    imgh = get_h(newImg)
    imgw = get_w(newImg)

    if(w > imgw):
        w = imgw
    if(h > imgh):
        h = imgh

    ma = ma[:h]
    mFinal = []
    for i in range(len(ma)):
        mFinal.append(ma[i][:w])

    return (form, mFinal)



    





