def valorMinimo(listaInteiros:list)->int:
    """
        Encontra o valor monimo de uma lista de inteiros e quantas vezes esse valor aparece na lista
        Entrada: lista de numeros inteiros, tipo lista
        Saida: quantidade de vezes que o valor minimo aparece na lista, tipo int
        >>> valorMinimo([1,5,1,7,9,1,6])
        3
        >>> valorMinimo([])
        0

        >>> valorMinimo([10,5,7,7,9,1,6])
        1
    """
    if len(listaInteiros) == 0:
        return 0
    
    valor_minimo:int = listaInteiros[0]
    n_aparicoes:int = 0


    #encontrar o valor minimo
    for x in range(1,len(listaInteiros)):
        if valor_minimo > listaInteiros[x]:
            valor_minimo = listaInteiros[x]

    #conta quantas vezes o valor minimo aparece
    for x in range(len(listaInteiros)):
        if valor_minimo == listaInteiros[x]:
            n_aparicoes += 1
    
    return n_aparicoes