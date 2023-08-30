def amplitudeDeDoisValores(listaInteiros:list)->int:
    """
        Encontra o maior e o menor valor em uma lista de inteiros, calcula a amplitude entre 
        esses dois valores e retorna esse valor

        >>> amplitudeDeDoisValores([1,2,6,7])
        6

        >>> amplitudeDeDoisValores([8,5,2,89])
        87
    """
    valor_minimo:int = listaInteiros[0]
    valor_maximo:int = listaInteiros[0]
    
    #encontra o menor valor 
    for x in range(1,len(listaInteiros)):
        if valor_minimo > listaInteiros[x]:
            valor_minimo = listaInteiros[x]
    
    #encontra o menor valor
    for x in range(1,len(listaInteiros)):
        if valor_maximo < listaInteiros[x]:
            valor_maximo = listaInteiros[x]

    return valor_maximo - valor_minimo