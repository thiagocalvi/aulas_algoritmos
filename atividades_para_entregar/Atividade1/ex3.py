def isTriangle(x:float, y:float, z:float) -> bool:

    """
        Recebe 3 valores X , Y , Z , respectivos lados de um triangulo
        verificar se os valores podem ser o comprimento dos lados de um triangulo
        >>> isTriangle(15.6, 45.0, 87.6)
        False
        >>> isTriangle(5.0, 7.0, 10.0)
        True
    """
    
    isTriangle : bool

    if x + y > z and x + z > y and y + z > x: 
        isTriangle = True
    else: 
        isTriangle = False

    return isTriangle


def tipoTriangulo(x:float, y:float, z:float) -> str:
    """
        Verifica o tipo do triangulo que é formado
        >>> tipoTriangulo(5.0, 5.0, 5.0)
        'Triângulo Equilátero'
        >>> tipoTriangulo(5.0, 7.0, 5.0)
        'Triângulo Isósceles'
        >>> tipoTriangulo(3.0, 4.0, 5.0)
        'Triângulo Escaleno'
    """
    tipo : str

    if x == y and y == z:
        tipo = "Triângulo Equilátero"
    
    elif x == y or x == z or y == z:
        tipo = "Triângulo Isósceles"
    
    else:
        tipo = "Triângulo Escaleno"

    return tipo


def main():
    x : float = float(input("Digite o valor do lado X: "))
    y : float = float(input("Digite o valor do lado Y: "))
    z : float = float(input("Digite o valor do lado Z: "))

    if isTriangle(x,y,z):
        print(tipoTriangulo(x,y,z))
    else:
        print("Não é possivel formar um triângulo")

main()