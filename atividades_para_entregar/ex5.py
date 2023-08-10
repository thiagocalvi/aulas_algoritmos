def valorCompra(quantidadeLaranjas:int) -> float:
    """
        Recebe a quantidade de laranjas compradas, calcula e retorna o valor total da compra em reais
        Cada laranja custa R$0,35 se comprado menos de uma duzia, se comprado uma dizia ou mais cada 
        laranja custa R$0,30
        >>> valorCompra(12)
        '3.60'
        >>> valorCompra(5)
        '1.75'
    """
    totalCompra : float

    if quantidadeLaranjas >= 12:
        totalCompra = quantidadeLaranjas * 0.30
    else:
        totalCompra = quantidadeLaranjas * 0.35

    totalCompra = "{:.2f}".format(totalCompra)

    return totalCompra 


def lerEntrada() -> str:
    quantidadeLaranja = int(input("Informe a quantidade de laranjas compradas: \n"))
    totalCompra = valorCompra(quantidadeLaranja)

    print(f"Valor total da compra R${totalCompra}")

lerEntrada()