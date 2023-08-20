def max_advance(linha, coluna, direcao):
    """
        Recebe as coordenadas do personagem no tabuleiro linha e coluna (int) e a direção que 
        pretende andar (string), retorna o numero de casas que é possivel andar (int)
        >>> max_advance(10, 10, 'sul')
        0
        >>> max_advance(10, 2, 'norte')
        9
    """

    direcao = direcao.upper()
 
    max_linha = 10
    max_coluna = 10
    min_linha = 1
    min_coluna = 1

    max_avanco = 0
    
    if direcao == "NORTE":
        max_avanco = linha - min_linha
    elif direcao == "SUL":
        max_avanco = max_linha - linha
    elif direcao == "LESTE":
        max_avanco = max_coluna - coluna
    elif direcao == "OESTE":
        max_avanco = coluna - min_coluna
    
    return max_avanco

def main():
    """
        Recebe a posição do personagem e a direção que quer andar e passa como parametro para 
        max_advance
    """
    print("""
        Para o número de linha e coluna informe números entre 1 e 10
        Opções para direção:
        Norte
        Sul
        Leste
        Oeste 

    """)

    linha : int = int(input('Número da linha: '))
    coluna : int = int(input('Número da coluna: ')) 
    direcao : str = input('Direção: ') 
    
    max_casas = max_advance(linha, coluna, direcao)

    if max_casas != 0:
        print(f"Pode avançar no máximo {max_casas} casas na direção {direcao}.")
    else:
        print(f"Não se pode avançar casas na direção {direcao}.")

main()