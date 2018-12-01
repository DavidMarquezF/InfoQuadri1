def mapatgecolor(temp):
    if(temp < 0):
        c = "Blanc"
    elif (temp >= 0 and temp <= 5):
        c="Violeta"
    elif (temp > 5 and temp <= 10):
        c ="Blau fosc"
    elif(temp > 10 and temp < 15):
        c="Blau clar"
    else:
        c = "Verd"
    return c

if __name__=='__main__':
    print mapatgecolor(input("Digues una temperatura: "))
