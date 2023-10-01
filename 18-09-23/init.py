#Exercicio
#Fatorial de um numeros
def fatorial(num):
    """
        fatorial(5)
        120
    """

    resultado = 1
    for x in range(1,num):
        resultado *= x+1
    
    return resultado


# Numero perfeito
def perfeito(num):
    """
        perfeito(6)
        True
    """
    #verificar quem são os seus divisores e salvar em uma lista
    divisores = []
    somaDivisores = 0
    
    if num == 1:
        return True


    for x in range(1,num):
        if num % x == 0:
            divisores.append(x)

    for x in divisores:
        somaDivisores += x

    if somaDivisores == num:
        return True
    else:
        return False