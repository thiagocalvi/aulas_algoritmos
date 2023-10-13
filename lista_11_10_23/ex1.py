def soma(lista:list[int])->int:
    """
    Recursivamente soma os elementos da lista
    >>> soma([1,2,3,4])
    10
    >>> soma([3])
    3
    """
    if len(lista) == 0:
        return 0
    
    else:
        return soma(lista[1:]) + lista[0]