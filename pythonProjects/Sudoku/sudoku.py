def chequejaCaixa(m):
    """
    >>> chequejaCaixa([[2,7,6,3,1,4,9,5,8],[8,5,4,9,6,2,7,1,3],[9,1,3,8,7,5,2,6,4],[4, 6, 8, 1, 2, 7, 3, 9, 5], [ 5, 9, 7, 4, 3, 8, 6, 2, 1], [1, 3, 2, 5, 9, 6, 4, 8, 7],[3, 2, 5, 7, 8, 9, 1, 4, 6], [6, 4, 1, 2, 5, 3, 8, 7, 9], [7, 8, 9, 6, 4, 1, 5, 3, 2]])
    True
    >>> chequejaCaixa([[2,7,5,3,1,4,9,6,8],[8,5,4,9,6,2,7,1,3],[9,1,3,8,7,5,2,6,4],[4, 6, 8, 1, 2, 7, 3, 9, 5], [5, 9, 7, 4, 3, 8,  6, 2,1],[1,3,2,5,9,6,4,8,7],[3,2,5,7,8,9,1,4,6],[6,4,1,2,5,3,8,7,9],[7,8,9,6,4,1,5,3,2]])
    False
    """
    for caixaX in range(3):
        for caixaY in range(3):
            #Per una caixa
            numsUtilitzats =""
            for i in range (caixaX*3, caixaX*3 + 3):
                for j in range(caixaY*3, caixaY*3 + 3):
                    if(m[i][j] < 1 or m[i][j] > 9):
                        return False
                    if(str(m[i][j]) in numsUtilitzats):
                        return False
                    numsUtilitzats += str(m[i][j])
    return True



