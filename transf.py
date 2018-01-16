#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  PIL
from PIL import Image
import img

def vtrim(imtg):
    """
    Retorna la imatge resultant de retallar-la verticalent. Si la imatge és blanca, retorna una imatge nula.
    >>> vtrim(('1',[[255,255,0],[255,0,255],[0,255,255]]))
    ('1', [[255, 255, 0], [255, 0, 255], [0, 255, 255]])
    >>> vtrim(('1',[[255,255,255],[255,255,255],[255,255,255]]))
    ('NULL', None)
    >>> vtrim(('1',[[255,255,255],[255,0,255],[0,255,255]]))
    ('1', [[255, 0, 255], [0, 255, 255]])
    >>> vtrim(('1',[[255,255,255],[0,0,0],[255,255,255]]))
    ('1', [[0, 0, 0]])
    """

    if imtg[0]!='1':
        raise Exception("La imatge no està en blanc i negre.")
    imatge=imtg[1]
    imgN=[]
    pFila=-1
    uFila=-1
    if imatge==[[255]*len(imatge[-1])]*len(imatge):
        return img.null()
    for i,j in enumerate(imatge):
        if j!=[255]*len(j):
            pFila=i
            break
    if pFila!=-1:
        for i in range(pFila,len(imatge)):
            imgN+=[imatge[i]]
    for i,j in enumerate(imatge[::-1]):
        if j!=[255]*len(j):
            uFila=i
            break
    if uFila!=-1:
        imgN=imgN[:len(imgN)-uFila]
    else:
        imgN=imatge
    return ('1',imgN)

def htrim(imtg):
    """
    Retorna la imatge resultant de retallar-la horitzontalment. SI la imatge és blanca, retorna una imatge nula.
    >>> htrim(('1',[[255,255,0],[255,0,255],[0,255,255]]))
    ('1', [[255, 255, 0], [255, 0, 255], [0, 255, 255]])
    >>> htrim(('1',[[255,255,255],[255,255,255],[255,255,255]]))
    ('NULL', None)
    >>> htrim(('1',[[255,255,255],[255,0,255],[0,255,255]]))
    ('1', [[255, 255], [255, 0], [0, 255]])
    """
    if imtg[0]!='1':
        raise Exception("La imatge no està en blanc i negre")
    imatge=imtg[1]
    imgN=[]
    r=-1
    if imatge==[[255]*len(imatge[-1])]*len(imatge):
        return img.null()
    for j in range(0,len(imatge)):
        col=[]
        for i in range(0,len(imatge[-1])):
            col+=[imatge[i][j]]
        if col==[255]*len(col):
            r=j
    if r!=-1:
        for i in range(0,len(imatge)):
            col=[]
            for j in range(0,r):
                col+=[imatge[i][j]]
            imgN+=[col]
    else:
        imgN=imatge
    return ('1',imgN)


def scale(imtg, h):
    """
    Escala homogèniament img fins que la seva alçada és h. S'usarà principalment per reduir la mida d'una imatge.
    >>> scale(("RGB", [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]),2)
    ('1', [[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]])
    >>> scale(("RGB", [[(0, 0, 0), (255, 255, 255), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),(255, 255, 255)], [(0, 0, 255), (255, 255, 255), (255, 255, 255)]]),2)
    ('1', [[(0, 0, 0), (255, 0, 0)], [(0, 0, 255), (255, 255, 255)]])
    >>> scale(("RGB", [[(0, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),(255, 255, 255), (255, 0, 0)], [(0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0)]]),2)
    ('1', [[(0, 0, 0), (255, 0, 0)], [(0, 0, 255), (255, 0, 0)]])
    >>> scale(("RGB", [[(0, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0)], [(0, 0, 0), (255, 255, 255), (255, 0, 0), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),(255, 255, 255), (255, 0, 0)], [(0, 0, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0)]]),2)
    ('1', [[(0, 0, 0), (255, 0, 0)], [(0, 0, 255), (255, 0, 0)]])
    >>> scale(("RGB", [[1,2,3,4],[5,6,7,8],[1,2,3,4]]),2)
    ('1', [[1, 4], [1, 4]])
    >>> scale (("RGB",[[1,2,3],[4,5,6],[7,8,9],[1,2,3]]),2)
    ('1', [[2], [2]])
    >>> scale(("RGB",[[1,2,3],[4,5,6],[7,8,9]]),2)
    ('1', [[1, 3], [7, 9]])
    """
    imatge = imtg[1]
    H = img.get_h(imtg)
    W = img.get_w(imtg)
    w = h * W / H
    fh=H/(h+.0)
    iscale = []

    for i in range(0, h):
        fila = []
        for j in range(0, w):
            fila += [0]
        iscale += [fila]

    for fila in range(h):
        for columna in range(w):
            iscale[fila][columna]=imatge[int(round(fila*fh))][int(round(columna*fh))]
    return ('1',iscale)



