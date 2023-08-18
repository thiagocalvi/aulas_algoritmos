def max_advance(linha, coluna, direcao):
    # Definindo os limites do tabuleiro
    max_linha = 10
    max_coluna = 10
    min_linha = 1
    min_coluna = 1

    max_advance = 0
    
    if direcao == "norte":
        max_advance = linha - min_linha
    elif direcao == "sul":
        max_advance = max_linha - linha
    elif direcao == "leste":
        max_advance = max_coluna - coluna
    elif direcao == "oeste":
        max_advance = coluna - min_coluna
    
    return max_advance

def main():
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: ')) 
    direcao = input('Direção: ') 
    
    max_casas = max_advance(linha, coluna, direcao)
    print(f"O personagem pode avançar no máximo {max_casas} casas na direção {direcao}.")


main()