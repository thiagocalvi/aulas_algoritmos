def e_binario(A, n):
    """
    Verifica se um array é binário
    
    >>> e_binario([0, 1, 0, 1], 4)
    True
    >>> e_binario([0, 1, 2, 1], 4) 
    False
    """
    if n == 0:
        return True
    if A[n-1] != 0 and A[n-1] != 1:
        return False
    else:
        return e_binario(A, n-1)