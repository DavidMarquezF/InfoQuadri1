import string
def aPerA(s):
    z=""
    for e in s:
        if(e == "a"):
            z+="A"
        else:
            z += e
    print z

def eliminaVocals(s):
    z = ""
    for e in s:
        if(e not in "aeiou"):
            z +=e
    return z

def hls(s):
    pos = s.find("que")
    print pos
s="Hola papa es festa major"
aPerA(s)
c = s.replace("a", "A")
print c
h = "Hola"
print h[::-1]

y = eliminaVocals(s)
y = y[1:10]
z = ""
for i, e in enumerate(y):
    if(i % 3  == 0 and i != 0):
        z+="bogeria"
    z+=e
print z
hls("que")
