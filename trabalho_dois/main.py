from dataset import provas

def somatorio_alternativas(s: int) -> list[int]:
    '''
    Calcula a lista de alternativas que somadas gera o somátorio *s*.
    Cada alternativa pode ser um dos valores: 1, 2, 4, 8, 16.
    Requer que *s* esteja no entre 0 e 31.
    Exemplos
    >>> somatorio_alternativas(0)
    []
    >>> somatorio_alternativas(1)
    [1]
    >>> somatorio_alternativas(21)
    [1, 4, 16]
    >>> somatorio_alternativas(10)
    [2, 8]
    >>> somatorio_alternativas(31)
    [1, 2, 4, 8, 16]
    '''
    alternativas = []
    alternativa = 1
    
    while s > 0:
    # verifica se alternativa faz parte do somatório s
        if s % 2 == 1:
            alternativas.append(alternativa)
    
        # divide todas as alternativas que compõe
        # o somatório s por 2
        s = s // 2
        # procura a próxima alternativa
        alternativa = alternativa * 2
    
    return alternativas

def nota_questao(resp_questao:int, gabarito_questao:int)->float:

  """Calcula a nota de uma questão comparando resposta e gabarito.

  Exemplos:

  >>> nota_questao(1, 1)
  6.0

  >>> nota_questao(2, 4)
  0.0

  >>> nota_questao(4, 8) 
  0.0

  >>> nota_questao(16, 4)
  0.0

  >>> nota_questao(8, 10)
  3.0
  """

  alternativas_resp:list[int] = somatorio_alternativas(resp_questao)
  alternativas_gabarito:list[int] = somatorio_alternativas(gabarito_questao)

  nota:float = 0.0
  q_alternativas_corretas:int = 0
  valor_questao:float = 6 / len(alternativas_gabarito) # Quanto cada questão esta valendo

  for alternativa in alternativas_resp:
    if alternativa not in alternativas_gabarito:
      # Se o candidato assinalou alguma alternativa errada, a nota da questão é zero
      return nota

    else:
      q_alternativas_corretas += 1 # Quantidade de altenativas corretas que o candidato assinalou

  
  nota = valor_questao * q_alternativas_corretas

  return nota

def calcula_notas(provas:list[list[int]], gabarito:list[int])->list[tuple]:
  """
  Calcula as notas de cada prova comparando com o gabarito
  
  Exemplos:
  >>> calcula_notas([[6716, 84, 13, 7, 11, 28, 14, 16, 28, 12, 25, 1, 23, 5, 21, 13, 11, 1, 3, 12, 30, 11, 28, 20, 0, 6, 26, 24, 16, 3, 17, 13, 19, 27, 20, 20, 26, 11, 28, 14, 26, 22, 23, 10, 11, 31, 3, 12, 5, 11, 5, 13],[9981, 26, 19, 20, 16, 26, 27, 29, 30, 19, 22, 8, 14, 18, 15, 27, 13, 8, 7, 31, 25, 19, 19, 31, 17, 16, 11, 17, 14, 9, 10, 28, 5, 14, 30, 15, 11, 13, 12, 8, 26, 27, 8, 10, 13, 19, 1, 13, 26, 28, 20, 20]], [22, 1, 3, 3, 27, 29, 27, 5, 25, 21, 15, 12, 2, 23, 17, 21, 4, 1, 16, 29, 27, 29, 29, 13, 11, 10, 6, 6, 5, 21, 24, 17, 4, 10, 28, 11, 8, 18, 6, 27, 8, 25, 22, 29, 23, 2, 25, 19, 2, 21])
  [(6716, 107.5), (9981, 73.5)]
  """
  
  notas:list[list] = []
  
  for prova in provas:
    nota:float
    codigo = prova[0]
    redacao = prova[1]
    respostas = prova[2:]
    
    if redacao > 0:
      nota = redacao
      
      for i in range(len(respostas)):
        nota += nota_questao(respostas[i], gabarito[i])
        
      notas.append((codigo, nota))

  return notas 

def ordena_por_nota(notas:list[tuple])->list[tuple]:
  """
  Ordena lista de notas em ordem decrescente de forma recursiva implementado quicksort
  
  Exemplos:
  >>> notas = [(3211, 80.0),(1234, 90.0),(2336, 108.0)]
  >>> ordena_por_nota(notas)
  [(2336, 108.0), (1234, 90.0), (3211, 80.0)]
  """

  if len(notas) <= 1:
    return notas
  
  else:
    pivot:list = notas[0]
    menores:list = []
    maiores:list = []

    for nota in notas[1:]:
      if nota[1] >= pivot[1]:
        maiores.append(nota)
      else:
        menores.append(nota)

    return ordena_por_nota(maiores) + [pivot] + ordena_por_nota(menores)

gabarito:list = [22, 1, 3, 3, 27, 29, 27, 5, 25, 21, 15, 12, 2, 23, 17, 21, 4, 1, 16, 29, 27, 29, 29, 13, 11, 10, 6, 6, 5, 21, 24, 17, 4, 10, 28, 11, 8, 18, 6, 27, 8, 25, 22, 29, 23, 2, 25, 19, 2, 21]

notas:list = calcula_notas(provas, gabarito)
notas_ordenadas:list[tuple] = ordena_por_nota(notas)

# Apresentação visual da notas
print("+--------------------------------+\n| Classificação | Código | Nota  |\n+--------------------------------+")
for colocacao, candidato in enumerate(notas_ordenadas, start=1):
    print(f"| {colocacao:13} | {candidato[0]:6} | {candidato[1]:4} |" + "\n+--------------------------------+" )
