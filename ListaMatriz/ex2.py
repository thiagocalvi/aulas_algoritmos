def divide_matriz(matriz):
    """Resebe uma matriz, calcula o maior valor da diagonal principal, divide toda a matriz por esse valor
        e cria um nova matriz com os resultados 
        >>> divide_matriz([[1,2,3],[4,5,6],[7,8,9]])
        [[0.1111111111111111, 0.2222222222222222, 0.3333333333333333], [0.4444444444444444, 0.5555555555555556, 0.6666666666666666], [0.7777777777777778, 0.8888888888888888, 1.0]]
        """
    maior = max(matriz[i][i] for i in range(3))
    
    resultado = [[0,0,0], [0,0,0], [0,0,0]]
    
    for i in range(3):
        for j in range(3):
            resultado[i][j] = matriz[i][j] / maior
    
    return resultado