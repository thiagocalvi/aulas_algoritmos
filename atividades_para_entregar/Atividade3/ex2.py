def verificaLista(lista: list) -> bool:
    """
        Recebe uma lista de numeros e verifica se a lista é não decresente
        Entra: Lista de numeros (number)
        Saida: True se a lista não for decresente, False se a lista for decresente (bool)

        >>> verificaLista([5,1,6,7,8,9])
        False
        
        >>> verificaLista([1,2,5,7,8,9,12])
        True
    """
    cresente = False
    atual = lista[0]

    for x in range(1, len(lista)):
        if atual < lista[x]:
            atual = lista[x]
            cresente = True
        else:
            return False

    return cresente