def unio(s,c):
    """
    retorna la unio entre c, s i c
    >>> unio("Hola", "Mon")
    'MonHolaMon'
    >>> unio("a", "")
    'a'
    """
    return  c + s + c

if __name__ == "__main__":
    unio("AA", "BA")