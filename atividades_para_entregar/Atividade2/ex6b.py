def verificaSobrepoem(window1_left:int, window1_top:int, window1_right:int, window1_bottom:int, 
                       window2_left:int, window2_top:int, window2_right:int, window2_bottom:int) -> bool:
    """
    Verifica se duas janelas se sobrepõem a partir das coordenadas recebidas por parametros.
    
    Entradas:
    window1_left, window1_top, window1_right, window1_bottom: Coordenadas da primeira janela (int).
    window2_left, window2_top, window2_right, window2_bottom: Coordenadas da segunda janela (int).
    
    Retorno:
    True se as janelas se sobrepõem, False caso contrário.

    >>> verificaSobrepoem(0, 0, 2, 2, 1, 1, 2, 2)
    True
    >>> verificaSobrepoem(0, 0, 1, 1, 2, 2, 1, 1)
    False
    
    """
    
    if (window1_left <= window2_right and window1_right >= window2_left and
        window1_top <= window2_bottom and window1_bottom >= window2_top):
        return True
    else:
        return False
