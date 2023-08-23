"""
    Verificar se uma lista está em ordem crescente
"""


def verifica(lista: list):
    cresente = False

    atual = lista[0]

    for x in range(1, len(lista)):
        if atual < lista[x]:
            atual = lista[x]
            cresente = True
        else:
            cresente = False

    if cresente:
        print("Lista não decrescente")
    else:
        print("Lista decrescente")
