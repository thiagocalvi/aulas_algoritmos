def area_retangulo(altura, base:float)->float:
    return base * altura


def retangulo():
    base = float(input('Digite o valor da base: '))
    altura = float(input('Digite o valor da altura: '))
    area = area_retangulo(altura, base)
    print('Area do retangulo',area)