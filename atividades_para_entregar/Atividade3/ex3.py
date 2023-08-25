def verifica(q_cand1:int, q_cand2:int, q_branco:int, q_invalido:int, votosInvalido:list) -> str:
    
    if q_branco > (q_cand1 + q_cand2):
        print("Quantidade de votos em branco é maior igual que 50%. \n Novas eleições!")
    else:
        if q_cand1 > q_cand2:
            print("Vencerdor das eleiçõse candidato 1")
        else:
            print("Vencerdor das eleiçõse candidato 2")
    
    print(f"""
        Total de votos: {q_cand1 + q_cand2 + q_branco + q_invalido}
        Total de votos validos: {(q_cand1 + q_cand2 + q_branco + q_invalido) - q_invalido}
        Total de votos candidato 1: {q_cand1}
        Total de votos candidato 2: {q_cand2}
        Total de votos em branco: {q_branco}
        Votos invalidos: {votosInvalido}

""")

def contaVotos(listaVotos:list) -> int:
    """
        Recebe uma lista com os votos da eleição votos do candidato 1, candidato 2 e votos em branco, 
        e faz a contagem desses votos, O para o candidato 1, T para o candidato 2 e W para voto em 
        branco (todas as entradas em maiusculo)
        Entrada: lista com os votos (list)(string)
        Saida: quantidade de votos candidato 1 (int), candidato 2 (int), em branco (int), invalido (int),
        lista de votos invalido (list)
          
        >>> contaVotos(['W','O','D','O','T','T'])
        (2, 2, 1, 1, ['D'])

        >>> contaVotos(['S','O','D','O','T','T'])
        (2, 2, 0, 2, ['S', 'D'])
    """
    q_cand1:int = 0
    q_cand2:int = 0
    q_branco:int = 0
    q_invalido:int = 0
    
    votosInvalido = []

    for x in range(len(listaVotos)):
        
        if listaVotos[x] == 'O':
            q_cand1 += 1
        elif listaVotos[x] == 'T':
            q_cand2 += 1
        elif listaVotos[x] == 'W': 
            q_branco += 1
        else:
            votosInvalido.append(listaVotos[x])
            q_invalido += 1
    
    return q_cand1, q_cand2, q_branco, q_invalido, votosInvalido






def main():
    votos = contaVotos(['W','O','D','O','T','T'])
    verifica(votos[0], votos[1], votos[2], votos[3], votos[4])