"""
    Receber uma lista de numeros dinamicos, um posição i da lista e um numero n,
    faz a inserção desse numero n na posição i e retorna a lista resultante

    >>> insertNumber([1,2,3,4,5,6,7,8,9,10,11],2,8)
    [1, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

"""

def insertNumber(lista:list, i:int, numero)->list:
    
    #indexs ocupado 
    ocupado:int = len(lista) - 1
    ultimoElemento = lista[len(lista) - 1]

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
    
print(insertNumber([1,2,3,4,5,6,7,8,9,10,11],2,8))