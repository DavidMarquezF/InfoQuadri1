import math

def tauladeMultiplicar(num, num2):
    print "La taula de multiplicar del", num
    i = num2
    while i >= 0:
        print num, "*", i, "=", num*i
        i-=1

def taulesdeMult():
    i = 0
    while i < 10:
        print "Taula  del", i
        tauladeMultiplicar(i, 10)
        i+=1

def factorial(num):
    print "El factorial de", num, "es", math.factorial(num)

def fac1100():
    i = 0
    while i < 101:
        print "Factorial de", i, "=",
        factorial(i)
        i+=1

num = input("Introdueix un nombre: ")
num2 = input("Introdueix un nombre: ")

tauladeMultiplicar(num, num2)
factorial(num)
taulesdeMult()
fac1100()