"""
    Receber uma lista de numeros dinamicos, um posição i e um numero n
    fazer a inserção desse numero n na posição i 

"""

def insertNumber(lista:list, i:int, numero)->list:
    
    #index ocupado 
    ocupado:int = len(lista) - 1
    
    if i-1 > ocupado:
        return ["Error, index não existe"] 

    for x in range(i-1, ocupado):

        elementoAtual = lista[x] #elemento atual  
        nextElement = lista[x+1] #proximo elemento da sequencia

        lista[x+1] = elementoAtual

        elementoAtual = nextElement

    lista[i-1] = numero

    return lista
    
print(insertNumber([1,2,3,4,5,6],2,8))