def pitagoras(b, c:float)->float:
    h = ((b**2) + (c**2))**(1/2)
    return h

def lerCatetos():
    b = float(input('Informe o cateto oposto: '))
    c = float(input('Informe o cateto adjacente: '))

    a = pitagoras(b,c)

    print('hipotenusa = ', a)