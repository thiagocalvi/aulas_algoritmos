def verificarLista(lista:list)->bool:
    """
        Verificar se todos os elementos de uma lista
        de booleanos são do tipo False, se forem retorna
        True caso contrario retorna Fase
        
        >>> verificarLista([False, True])
        False

        >>> verificarLista([False, False])
        True
    """
    todosFalso:bool = False

    for x in range(len(lista)):
        
        if lista[x] == False:
            todosFalso = True
        else:
            todosFalso = False
    
    return todosFalso
