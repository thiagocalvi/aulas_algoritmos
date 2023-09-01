def amplitudeDeDoisValores(listaInteiros:list)->int:
    """
        Encontra o maior e o menor valor em uma lista de inteiros, calcula a amplitude entre 
        esses dois valores e retorna esse valor
        Entrada: lista de inteiros, tipo lista
        Saida: valor de amplitude entre o valor minimo e maximo, tipo int

        >>> amplitudeDeDoisValores([1,2,6,7])
        6

        >>> amplitudeDeDoisValores([8,5,2,89])
        87
    """

    valor_minimo:int = listaInteiros[0]
    valor_maximo:int = listaInteiros[0]
    amplitude:int = 0
        
    for x in range(1,len(listaInteiros)):
        
        #encontra o valor minimo
        if valor_minimo > listaInteiros[x]:
            valor_minimo = listaInteiros[x]
        
        #encontra o valor maximo
        if valor_maximo < listaInteiros[x]:
            valor_maximo = listaInteiros[x]

    amplitude = valor_maximo - valor_minimo

    return amplitude