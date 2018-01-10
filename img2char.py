import sys, discret, img, imgio,match,split,transf

if(__name__ =="__main__"):
    s = sys.argv[1:]
    patrons = s[0]
    matricula = s[1]
    patronsImg = match.load_patterns(patrons)
    for i, patro in enumerate(patronsImg):
        patronsImg[i] = discret.rgb_to_bn(patro)


    matriculaImg = imgio.read_rgb(matricula)
    matriculaImg = discret.rgb_to_bn(matriculaImg)
    matriculaImg = transf.vtrim(matriculaImg)
    print matriculaImg
    hPatrons = img.get_h(patronsImg[0])
    matriculaImg = transf.scale(matriculaImg, hPatrons)

    matriculaNumbers = []
    matriculaSplit = matriculaImg
    while True:
        splt = split.split_digit(matriculaSplit)
        matriculaMatch = match.match(splt[0], patronsImg)
        matriculaNumbers.append(matriculaMatch)
        matriculaSplit = splt[1]
        if(len(matriculaSplit[1]) == 0):
            break
    print matriculaNumbers


