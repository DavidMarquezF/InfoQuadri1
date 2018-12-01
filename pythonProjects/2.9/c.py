import math

t = input("Digues un temps en segons: ")
l = (t/(2*math.pi))**2 * 9.81
print "La longitud del pendol que tindria aquest periode es de", l , "metres."
