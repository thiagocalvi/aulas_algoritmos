def verifica(name:str)->bool:
    name = name.upper()
    nameSeparado = name.split()
    lastName = nameSeparado[len(nameSeparado)-1]
    return lastName == 'SILVA'

def lerName():
    name = input('Informe seu nome completo: ')
    igual = verifica(name)
    print('Seu ultimo nome igual Silva ' , igual)