def encontraMaiorNumero(lista:list) -> int:
    """
        Recebe como paramentro uma lista de dumeros, retorna o maior numero da lista e seu index
        >>> encontraMaiorNumero([1,24,5,89,100,555])
        (555, 5)

        >>> encontraMaiorNumero([-4,4,89,289559,1033,4599])
        (289559, 3)
    """
    maiorNumero : list = lista[0]
    posicao = 0

    for x in range(1, len(lista)):
        if lista[x] > maiorNumero:
            posicao = x
            maiorNumero = lista[x]

    return maiorNumero, posicao




def main():
    dados = encontraMaiorNumero([1,24,5,89,100,555,0])
    print(f'Maior número da lista: {dados[0]}, na posiçao: {dados[1]}')


main()