def primos_ate(n):
  """Recebe um numero N inteiro e retorna uma lista com todos os numeros primos até N
    >>> primos_ate(10)
    [2, 3, 5, 7]
  """
  primos = []
  for i in range(2, n+1):
    é_primo = True
    for p in primos:
      if i % p == 0:
        é_primo = False
        break
    if é_primo:
      primos.append(i)
  return primos
