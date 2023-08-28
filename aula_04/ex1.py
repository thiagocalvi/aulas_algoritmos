# loop while
lista: list = ['a', 'b', 'c']

def verificaElementoNaLista(lista: list, elemneto) -> bool:
    """
        Verifica se um elemento esta contido em uma lista
        >>> verificaElementoNaLista(['a', 'b', 'c'], 'a'))
        True
        >>> verificaElementoNaLista(['a', 'b', 'c'], 'o'))
        False
    """
    
    inList: bool = False
    indexOfElement: int = 0

    while not inList and indexOfElement < (len(lista)-1):
        if lista[indexOfElement] == elemneto:
            inList = True
        indexOfElement += 1

    return inList


