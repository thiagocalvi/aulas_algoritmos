def proximaCorSemafaro(corAtual : str) -> str:
    """
        Recebe uma cor de semáfaro com entrada e 
        retorna a próxima cor que será ativada
        Entrada: cor atual do semáfaro (string)
        Saída: próxima cor do semáfaro (string)
        >>> proximaCorSemafaro('Verde')
        'Amarelo'
        >>> proximaCorSemafaro('Vermelho')
        'Verde'
        >>> proximaCorSemafaro('Amarelo')
        'Vermelho'
    """
    corAtual = corAtual.upper()

    if corAtual == "VERDE":
        proximaCor = "Amarelo"
    elif corAtual == "AMARELO":
        proximaCor = "Vermelho"
    else:
        proximaCor = "Verde"
    
    return proximaCor


def main():
    cor_atul : str = input('Informe a cor atual do semáfaro: ')
    next_cor : str = proximaCorSemafaro(cor_atul)
    print(next_cor)

main()