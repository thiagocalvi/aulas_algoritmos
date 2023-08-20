"""
    Receber o tamanho de uma janela e as coordenas de um click, verificar se o click aconteceu dentro
    da janela
"""


def click_na_janela(janela_top:int, janela_bottom:int, janela_left:int, janela_right:int, click_x:int, click_y:int) -> bool:
    """
        Recebe as informações do tamanho da janela e as coordenadas do click e verifica se o click aconteceu
        dentro da janela se sim retorna True caso contrario retorna False
        >>> click_na_janela(0, 100, 0, 100, 50, 50)
        True
        >>> click_na_janela(0, 100, 0, 100, -10, 150)
        False
    """
    if janela_top <= click_y <= janela_bottom and janela_left <= click_x <= janela_right:
        return True
    else:
        return False

def main():
    #Receber as informações do tamanho da janela
    janela_top : int =  int(input('Informe o top da janela: '))
    janela_bottom : int =  int(input('Informe o bottom da janela: '))
    janela_left : int =  int(input('Informe o left da janela: '))
    janela_right : int =  int(input('Informe o right da janela: '))

    #coordenadas do onde foi feito o click eixo X e Y
    click_x : int =  int(input('Informe a posição do click eixo x: '))
    click_y : int =  int(input('Informe a posição do click eixo y: '))

    #chama a função click_na_janela para verificar se o click foi feito dentro da janela
    if click_na_janela(janela_top, janela_bottom, janela_left, janela_right, click_x, click_y):
        print('Click na janela')
    else:
        print('Click fora da janela')

main()
