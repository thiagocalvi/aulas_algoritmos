
def mediaIdades(idade1:int, idade2:int, idade3:int, idade4:int) -> float:
    """
        Recebe 4 idades e calcula a media entre elas,
        (idade1 + idade2 + idade3 + idade4) / 4

        >>> mediaIdades(12,23,56,89)
        45.0
        >>> mediaIdades(58,89,23,36)
        51.5
    """
    
    media = (idade1 + idade2 + idade3 + idade4) / 4

    return float(media)


def maiorIdade(idade1:int, idade2:int, idade3:int, idade4:int) -> int:
    """
        >>> maiorIdade(58,23,56,89)
        89
        >>> maiorIdade(88,27,16,52)
        88
    """


    maior : int

    if idade1 > idade2 and idade1 > idade3 and idade1 > idade4:
        maior = idade1
    elif idade2 > idade3 and idade2 > idade4:
        maior = idade2
    elif idade3 > idade4:
        maior = idade3
    else: 
        maior = idade4
        
    return maior


def main():
    idade1 = int(input("Informe a idade da primeira pessoa: \n"))
    idade2 = int(input("Informe a idade da segunda pessoa: \n"))
    idade3 = int(input("Informe a idade da terceira pessoa: \n"))
    idade4 = int(input("Informe a idade da quarta pessoa: \n"))
    
    media : float = mediaIdades(idade1,idade2, idade3, idade4)

    idadeMaior : int = maiorIdade(idade1, idade2, idade3, idade4)

    print(f"Calculo da media das idades: {media}\nIdade da pessoa mais velha: {idadeMaior}")

main()