def sao_pares(A, n):
    """
    Verifica se todos elementos de um array são pares
    
    >>> sao_pares([2, 4, 6, 8], 4)
    True
    >>> sao_pares([1, 3, 5, 7], 4)
    False
    """        
    if n == 0:
        return True
    if A[n-1] % 2 != 0:
        return False
    else:
        return sao_pares(A, n-1)