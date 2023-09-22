def soma_matriz(matriz):
  """Recebe uma matriz [4][3] e retorna a soma de todos os elementos da matriz
    >>> soma_matriz([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
    24
  """
  soma = 0
  
  for i in range(4):
    for j in range(3):
      soma += matriz[i][j]
  
  return soma


