def calculaPunts(euros):
    if(euros < 10):
        q=1
    else:
        q =int(euros)/5 *3
        q = int(q)
        if(euros >= 1000):
            q+=50
    return q

def actualitzaPunts(punts, euros):
    return punts + actualitzaPunts(euros)

