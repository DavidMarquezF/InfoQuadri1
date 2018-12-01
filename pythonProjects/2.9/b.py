import math

vel = input("Digues una velocitat de sortida en m/s: ")
anglegrau = input("Digues un angle de sortida en graus: ")

anglerad = anglegrau * 2 * math.pi / 360

velx = math.cos(anglerad)*vel
vely = math.sin(anglerad)*vel

x = velx * 2 * vely / 9.81
t = x / velx

print "La distancia recorreguda des del punt 0 sera", x, " metres"
print "Estara", t, "segons a l'aire"
