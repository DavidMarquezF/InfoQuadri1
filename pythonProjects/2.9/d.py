import math

capital = input("Digues el teu capital ingressat en euros: ")
taxaint = input("Digues la taxa d'interes anual en tant per cent: ")
anys = input ("Anys: ")

capFinal = capital * (1 + taxaint/100.0) ** anys

print "Al cap de", anys, "tindras un capital de", capFinal, "euros"

