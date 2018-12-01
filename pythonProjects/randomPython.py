#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def joc(nom, inici, fi, oportunitats):
    endevina = random.randint(inici,fi)
    print "Endevinant el nombre..."
    i = 0
    t= False
    while(i < oportunitats and not t):
        n = input("Entri un nombre... ")
        if(n == endevina):
            print "Ho has endevinat al", i + 1, "intent"
            t=True
        elif n < endevina:
            print "El nombre és més gran,", nom
    
        elif n > endevina:
            print "El nombre és més petit,", nom
        else:
            print "No ho has endevinat"
        i+=1
    if(not t):
        print  nom, "el nombre era", endevina
    return t

def juga(nom):
    j = 1
    punts = 0
    jocsEnUn = input("Quantes rondes vols fer? ")
    while (j <= jocsEnUn):
        print "-------------ROUND", j, "-------------"
        inici = input("Digues l'inici de l'interval que vols endevinar: ")
        fi = input("Digues el fi de l'interval que vols endevinar: ")
        oportunitats = input("Quin nombre d'oportunitats vols? ")
        if(joc(nom, inici, fi, oportunitats)):
            punts+=1
        j+=1
    print "-------------GAME OVER-------------"
    print "Puntuació:", punts
    
if(__name__=="__main__"):
    nom = raw_input("Com et dius? ")
    continuar = "Y"
    while(continuar == "Y" or continuar == "y"):
        juga (nom)
        continuar = raw_input("Vols tornar a jugar? (Y/N)")
        if(continuar == "N" or continuar == "n"):
            print "Adéu"
        else:
            while (continuar != "N" and continuar != "n" and continuar != "Y" and continuar != "y"):
                print "Opció no vàlida"
                continuar = raw_input("Vols tornar a jugar? (Y/N)")

    
    
