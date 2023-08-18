def do_windows_overlap(window1_left, window1_top, window1_right, window1_bottom, 
                       window2_left, window2_top, window2_right, window2_bottom):
    """
    Verifica se duas janelas se sobrepõem.
    
    Parâmetros:
    window1_left, window1_top, window1_right, window1_bottom: Coordenadas da primeira janela.
    window2_left, window2_top, window2_right, window2_bottom: Coordenadas da segunda janela.
    
    Retorna:
    True se as janelas se sobrepõem, False caso contrário.
    """
    if (window1_left <= window2_right and window1_right >= window2_left and
        window1_top <= window2_bottom and window1_bottom >= window2_top):
        return True
    else:
        return False
