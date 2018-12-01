def festival (punts, pais):
    punts = "{:02}".format(punts)
    punts = str(punts)
    return (pais +": " + punts)

if __name__=='__main__':
    print festival(input("Introdueix la puntuacio: "), raw_input("Introdueix el pais: "))
