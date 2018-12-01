def obtainUrls(nom):
    f = open(nom)
    llista=[]
    for linia in f:
        if(linia.startswith("<a href")):
            start = linia.find('"') + 1
            if("#" not in linia):
                end = linia.find('"', start)
            else:
                end = linia.find('#', start)

            l = linia[start:end]
            if(l not in llista):
                llista.append(l)
    f.close()
    return llista

if(__name__ =="__main__"):
    print obtainUrls("web.html")
