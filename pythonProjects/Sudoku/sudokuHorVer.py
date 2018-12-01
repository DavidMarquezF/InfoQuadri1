def chequejaHorizontal (m):
    for i in range(len(m)):
        numsUtilitzats = ""
        for j in range(len(m[0])):
            if(m[i][j] in numsUtilitzats):
                return False
            numsUtilitzats += str(m[i][j])
    return True

def chequejaVertical (m):
    n = m[:]
    for i in range(len(m)):
        for j in range(len(m[0])):
            n[j][i] = m[i][j]
    return chequejaHorizontal(n)