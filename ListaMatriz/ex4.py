def n_primos(n:int)->list:
    """Recebe um numero N inteiro e retorna uma lista com os N primeiros numeros primos
    >>> n_primos(12)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    """
    cont = 0
    i = 2
    primos = []
    while cont < n:
        e_primo = True
        for p in primos:
            if i % p == 0:
                e_primo = False
                break
        if e_primo:
            primos.append(i)
            cont += 1
        i += 1
    return primos
