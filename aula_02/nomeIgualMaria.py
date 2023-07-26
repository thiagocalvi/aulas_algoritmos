def verifica(name:str)->bool:
    name = name.upper()
    nameSeparado = name.split()
    firstName = nameSeparado[0]
    return firstName == 'MARIA'


def lerName():
    name = input('Digite seu primeiro nome:')
    igual = verifica(name)
    print('Seu nome é igual Maria', igual)