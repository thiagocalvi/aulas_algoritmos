def insertNumber(lista:list, i:int, numero)->list:
    """
        Receber uma lista de numeros dinamicos, um posição i da lista e um numero n,
        faz a inserção desse numero n na posição i e retorna a lista resultante
        Entradas: lista de numoros, tipo lista. Posição da substituição, tipo inteiro. Numero que sera adicionado, tipo numerico
        Saida: nova lista com o numeros n na posição i 

        >>> insertNumber([1,2,3,4,5,6,7,8,9,10,11],2,8)
        [1, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        >>> insertNumber([1,2,3,4,5,6,7,8,9,10,11],4,12)
        [1, 2, 3, 12, 4, 5, 6, 7, 8, 9, 10, 11]

    """    
    #indexs ocupado 
    ocupado:int = len(lista) - 1
    ultimoElemento:list = lista[len(lista) - 1]

    if i-1 > ocupado or i-1 < 0:
        return ["Error, index não existe"] 

    elementoAtual = lista[i-1] #elemento atual 
    
    for x in range(i-1, ocupado): 
        
        nextElement = lista[x+1] #proximo elemento da sequencia

        lista[x+1] = elementoAtual

        elementoAtual = nextElement

    lista[i-1] = numero

    lista.append(ultimoElemento)

    return lista
