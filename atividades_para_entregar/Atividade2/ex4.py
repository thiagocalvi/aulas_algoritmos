"""
    Classificar um nome como curto, longo ou mediano
    baseado no número de letras
    Entradas: nome(string)
    Saída: classificação do nome(string)
"""
def classificarNome(nome : str) -> str:
    """
        Classifica o nome de acordo com a quantidade
        de letra
        >>> classificarNome('Pedro')
        'Mediano'
        >>> classificarNome('Josévaldo')
        'Longo'
    """
    
    qtde_letras : int = len(nome)

    if qtde_letras <= 4:
        classificacao = "Curto"
    elif qtde_letras >= 8:
        classificacao = "Longo"
    else:
        classificacao = "Mediano"

    return classificacao


def main():
    nome : str = input('Informe seu nome: ')
    classificacao : str = classificarNome(nome)
    print(f'Nome: {nome} \nClassificação: {classificacao}')

main()
