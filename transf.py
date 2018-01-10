#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    """
    if imtg[0]!='1':
        raise Exception("La imatge no està en blanc i negre")
    imatge=imtg[1]
    imgN=[]
    r=-1
    if imatge==[[255]*len(imatge[-1])]*len(imatge):
        return img.null()
    for i,j in enumerate(imatge):
        if j==[255]*len(j):
            r=i+1
    if r!=-1:
        for i in range(r,len(imatge)):
            imgN+=[imatge[i]]
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

def scale(img,h):
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
    """
    imatge=img[1]
    H=len(imatge)
    W=len(imatge[0])
    fh=(H/(h+.0))+0.5
    w=h*W/H
    fw=(W/(w+.0))+0.5
    iscale=[]
    for i in range(0,h):
        fila=[]
        for j in range(0,w):
            fila+=[0]
        iscale+=[fila]
    f=int(round(fh,0))
    v = int(round((fw), 0))
    for a in range(0,h):
        af=a*f
        for b in range(0,w):
            bf=b*(v)
            iscale[a][b]=imatge[af][bf]
    return ('1',iscale)