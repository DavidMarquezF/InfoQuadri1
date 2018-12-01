import math

def a():
    h = input("Digues una alcada: ")
    t = math.sqrt((2 * h) / 9.81)
    return "Trigara " + str(t) + " segons a arribar al terra."
def b():
    vel = input("Digues una velocitat de sortida en m/s: ")
    anglegrau = input("Digues un angle de sortida en graus: ")

    anglerad = anglegrau * 2 * math.pi / 360

    velx = math.cos(anglerad) * vel
    vely = math.sin(anglerad) * vel

    x = velx * 2 * vely / 9.81

    return "La distancia recorreguda des del punt 0 sera " +  str(x) + " metres"
def c():
    t = input("Digues un temps en segons: ")
    l = (t / (2 * math.pi)) ** 2 * 9.81
    return "La longitud del pendol que tindria aquest periode es de " + str(l) + " metres."
def d():
    capital = input("Digues el teu capital ingressat en euros: ")
    taxaint = input("Digues la taxa d'interes anual en tant per cent: ")
    anys = input("Anys: ")

    capFinal = capital * (1 + taxaint / 100.0) ** anys

    return "Al cap de " + str(anys) + " tindras un capital de " + str(capFinal) + " euros"

if __name__ == '__main__':
	print a()
	print b()
	print c()
	print d()
