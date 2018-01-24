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
    >>> htrim(('1',[[255,255,255,255],[255,255,0,255],[255,255,0,255]]))
    ('1', [[255], [0], [0]])
    """
    if imtg[0][0]!='1':
        
        raise Exception("La imatge no està en blanc i negre")
    imatge=imtg[1]
    imgN=[]
    pColumna=-1
    uColumna=-1
    if imatge==[[255]*len(imatge[-1])]*len(imatge):
        return img.null()
    pColumna=retallah(imatge,1)
    if pColumna!=-1:
        for i in range(0,len(imatge)):
            fila=imatge[i]
            imgN+=[fila[pColumna:]]
    else:
        imgN+=imatge
    uColumna=retallah(imgN,-1)
    if uColumna!=-1:
        for i in range(0,len(imgN)):
            fila=imgN[i]
            imgN[i]=fila[:uColumna+1]
    return ('1',imgN)


def retallah(imatge,p):
    Columna=-1
    t=False
    if p==1:
        a=0
        b=len(imatge[0])
    else:
        a=(len(imatge[0])-1)
        b=-1
    for col in range(a,b,p):
        columna=[]
        if t==True:                      
            break
        for fila in range(len(imatge)):
            columna+=[imatge[fila][col]]
        if columna!=[255]*len(imatge):
            Columna=col
            t=True

    return(Columna)

def scale(imtg, h):
    """
    Escala homogèniament img fins que la seva alçada és h. S'usarà principalment per reduir la mida d'una imatge.
    >>> scale(("RGB", [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]),2)
    ('RGB', [[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]])
    >>> scale(("RGB", [[(0, 0, 0), (255, 255, 255), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),(255, 255, 255)], [(0, 0, 255), (255, 255, 255), (255, 255, 255)]]),2)
    ('RGB', [[(0, 0, 0), (255, 0, 0)], [(0, 0, 255), (255, 255, 255)]])

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
    return (imtg[0],iscale)



