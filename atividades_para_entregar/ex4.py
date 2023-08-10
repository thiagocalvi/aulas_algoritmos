def conceitoNota(media:float) -> str:
    
    """
        Recebe por parametro a media da nota de um aluno e classifica esssa media em 
        um conceito:
        media maior a 8.9 e menor igual 10.0 = A
        media de 7.0 a 8.9 = B  
        media de 5.0 a 6.9 = C
        media menor igual a 4.9 = D

        >>> conceitoNota(5.8)
        'C'
        >>> conceitoNota(2.9)
        'D'
        >>> conceitoNota(8.4)
        'B'
        >>> conceitoNota(9.2)
        'A'
    """

    conceito : str

    if media <= 4.9:
        conceito = "D"
    elif media >= 5.0 and media <= 6.9:
        conceito = "C"
    elif media >= 7.0 and media <= 8.9:
        conceito = "B"
    elif media >= 9.0 and media <= 10.0: 
        conceito = "A"

    return conceito


def lerEntrada() -> str:
    mediaNota : float = float(input("Informe a media das notas do aluno: \n"))

    conceito : str = conceitoNota(mediaNota)

    print(f"Conceito da nota do aluno: {conceito}")

lerEntrada()