def construeix_llista(n):
    s = []
    for i in range(1, n+1):
        s+=[i**2]
    return s
def  quadrat(m):
    s = []
    for i in m:
        s+=[i**2]
    return s

def treureparell(m):
    s = []
    for i in range(len(m)):
        if(i % 2 != 0):
          s+=[m[i]]

    return s

def mitjana(m):
    to=0
    for e in m:
        to+=e
    return to/len(m)

print construeix_llista(5)
print quadrat([1,2,4,5])
print treureparell([1,2,3,4,5,6,7])
print mitjana([2,2,2])