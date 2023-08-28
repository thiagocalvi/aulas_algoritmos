def verificaLista(lista:list):
    """
        Verifica se uma lista tem menos que 4 elementos
        >>> verificaLista([0.1,2.3,1.4])
        True
        >>> verificaLista([0.1,2.3,1.4,10.2,45.8])
        False
    """
    menor:bool = False
    controller:bool = True
    indexLista:int = 0
    lenghLista:int = 0

    while controller:
        try:
            if type(lista[indexLista]) == float:
                lenghLista += 1 
                indexLista += 1
        
        except IndexError:
            
            controller = False
            
            if lenghLista < 4:
                menor = True
        
        
    return menor

