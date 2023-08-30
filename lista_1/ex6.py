def nomeNaLista(listaNomes:list, nome:str)->int:
    """
        Encontra todas as posicoes de ocorrencia de um nome recebido por
        parametro na lista e retorna suas posições
        
        >>> nomeNaLista(['ana','marcos','sergio','ana'], 'ana')
        [0, 3]
        
        >>> nomeNaLista(['pedro','marcos','cabral','josé','ana'], 'cabral')
        [2]
    """

    indexNome = []

    # listaNomes = toUpperCase(listaNomes)

    for i in range(len(listaNomes)):
        if listaNomes[i] == nome:
            indexNome.append(i)

    return indexNome