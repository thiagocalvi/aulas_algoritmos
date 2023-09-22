def cacapalavra(matriz, palavra):
  """Recebe uma matriz representando um caça-palavras e uma palavra, verifica todas as possições de 
      ocorrencia dessa palavra na matriz
  >>> cacapalavra([['A', 'C', 'A', 'S', 'A', 'M', 'C', 'A', 'S', 'W', 'B'],['C', 'A', 'X', 'R', 'F', 'T', 'P', 'A', 'S', 'A', 'C'], ['A', 'S', 'X', 'I', 'E', 'J', 'H', 'W', 'T', 'Q', 'A'],['S', 'A', 'E', 'O', 'W', 'M', 'Q', 'Z', 'O', 'D', 'B'],['A', 'C', 'Y', 'K', 'F', 'W', 'C', 'A', 'A', 'V', 'B']], "CASA")
  [(0, 1), (1, 0), (0, 1)]
    """
  ocorrencias = []
  # busca nas linhas
  for i in range(len(matriz)):
    for j in range(len(matriz[0]) - len(palavra)+1):
      if ''.join(matriz[i][j:j+len(palavra)]) == palavra:
        ocorrencias.append((i, j))
  
  # busca nas colunas
  for j in range(len(matriz[0])):
    for i in range(len(matriz) - len(palavra)+1):
      coluna = [matriz[k][j] for k in range(i, i+len(palavra))]
      if ''.join(coluna) == palavra:
        ocorrencias.append((i, j))

  return ocorrencias