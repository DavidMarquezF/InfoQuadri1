import math

def proper():
    primer = input("Escriu enter: ")
    proper = input("Escriu enter: ")
    i = 0
    while i < 3:
        num = input("Escriu enter: ")
        if(abs(primer - num) < abs(primer-proper)):
            proper=num
        i+=1
    print "El nombre", proper, "es el mes proper a", primer

proper()