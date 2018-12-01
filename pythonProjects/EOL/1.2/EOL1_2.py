def justificat_a_la_dreta(s):
    llargada = len(s)
    espais = 70 - llargada
    print " "*espais + s

if __name__ == '__main__':
    justificat_a_la_dreta(raw_input("Escrigui una paraula: "))
