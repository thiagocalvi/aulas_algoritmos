def somaElemento(listaInteiros:list)->int:
    """
        Recebe uma lista de inteiros e soma todos os elementos e retorna essa soma
        Entrada: lista de numeros inteiros, tipo lista
        Saida: resultado da soma de todos os elementos, tipo inteiro

        >>> somaElemento([1,2,3])
        6

        >>> somaElemento([1,2,3,4])
        10
    """

    soma:int = 0
    
    for x in range(len(listaInteiros)):
        soma += listaInteiros[x]
    
    return soma