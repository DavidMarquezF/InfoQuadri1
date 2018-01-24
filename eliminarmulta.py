#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string

def diccionari(fitxer):
    """
    Retorna un diccionari on l'index es la matricula
    """
    d={}
    f=open(fitxer,"r")
    for linia in f:
        linia=linia[:-1]
        g=linia.split("/")
        d[g[0]]=int(g[1])
    return d

def chekejaMatricula(matricula):
    """
    retorna True si la matricula existeix, sino retorna False
    """
    d=diccionari("multes.txt")
    if d.has_key(matricula):
        return True
    return False

def demanaMatricula():
    """
    retorna la matricula que s'ha demanat, iteria si no és correcte
    """

    t=False
    while  not t:
        matricula = raw_input("Introdueix matricula:")
        for i in matricula:
            if i not in string.digits:
                print"Matricula incorrecte."
                break
        else:
            return matricula
            t=True


def eliminaMatricula(fitxer):
    """
    Retorna el diccionari del fitxer sense la matricula que es vol eliminar
    """
    matricula=demanaMatricula()
    d=diccionari(fitxer)
    if d.has_key(matricula):
        del d[matricula]
    else:
        print "Matricula no registrada."
    return d





if __name__=='__main__':
    d=diccionari("multes.txt")
    d=eliminaMatricula("multes.txt")
    print d