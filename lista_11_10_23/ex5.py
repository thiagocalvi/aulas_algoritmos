def max_array(A, n):
    """
    Encontra o maior valor em um array
    
    >>> max_array([4, 2, 5, 1], 4)
    5
    >>> max_array([-2, 0, 10, -5], 4)
    10
    """
    if n == 1:
        return A[0]
    m = max_array(A, n-1)
    if A[n-1] > m:
        return A[n-1]
    else:
        return m