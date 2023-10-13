def frequencia(lista:list[int], n:int)->int:
    """
    Soma a frequencia de um n em lista
    >>> frequencia([1,2,1,3],1)
    2
    >>> frequencia([1,2,3,2,4,2],2)
    3
    """
    if len(lista) == 0:
        return 0
    else:
        if lista[0] == n:
            return frequencia(lista[1:], n) + 1
        else:
            return frequencia(lista[1:], n)