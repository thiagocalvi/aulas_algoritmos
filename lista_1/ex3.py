def verificaLista(listaInteiros:list) -> bool:
    """
        Verifica se todos os elemontos de uma 
        lista de inteiros e menor que 10, se forem
        retorna True caso contratario retorna False

        >>> verificaLista([1,2,5,10,78])
        False

        >>> verificaLista([8,1,4,9])
        True
    """
    isMenor:bool = True
        
    for x in range(len(listaInteiros)):
        
        if listaInteiros[x] > 10:
            isMenor = False
            return isMenor
    return isMenor