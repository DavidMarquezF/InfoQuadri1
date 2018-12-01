from math import ceil # ceil arrodoneix per exces

def calcula_quadrant(a):
    """
    retorna a quin quadrant pertany

    >>> calcula_quadrant(45)
    0
    >>> calcula_quadrant(105)
    1
    >>> calcula_quadrant(190)
    2
    >>> calcula_quadrant(340)
    3

    """
    return int(ceil(a) % 360) / 90

if(__name__ == "__main__"):
    angle = float(raw_input("Escriu un angle en graus: "))
    quadrant = calcula_quadrant(angle)
    if quadrant == 0:
       print "primer quadrant"
    elif quadrant == 1:
       print "segon quadrant"
    elif quadrant == 2:
       print "tercer quadrant"
    elif quadrant == 3:
       print "quart quadrant"