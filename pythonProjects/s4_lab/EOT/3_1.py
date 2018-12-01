def parellSenar(num):
    """
    Retorna True si el nombre es parell i False si es senar
    >>> parellSenar(2)
    True
    >>> parellSenar(-56)
    True
    >>> parellSenar(23)
    False

    """

    if(num % 2 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    parellSenar(2)