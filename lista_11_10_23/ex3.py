def esta_ordenado(A, n):
    """
    Verifica se um array está ordenado
    
    >>> esta_ordenado([1, 2, 3, 4], 4)
    True
    >>> esta_ordenado([4, 2, 1, 5], 4)
    False
    """
    if n == 1:
        return True
    if A[n-1] < A[n-2]:
        return False
    else:
        return esta_ordenado(A, n-1)