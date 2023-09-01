def nomeNaLista(listaNomes:list, nome:str)->int:
    """
        Encontra as posicoes de ocorrencia de um nome em uma lista e retorna suas posições
        Entradas: lista de nomes, tipo lista. Nome que se quer encontrar as posições, tipo string
        Saida: lista contendo as possições de ocorrencia do nome

        >>> nomeNaLista(['ana','marcos','sergio','ana'], 'ana')
        [0, 3]
        
        >>> nomeNaLista(['pedro','marcos','cabral','josé','ana'], 'cabral')
        [2]
    """

    indexNome:list = []

    for i in range(len(listaNomes)):
        if listaNomes[i] == nome:
            indexNome.append(i)

    return indexNome
