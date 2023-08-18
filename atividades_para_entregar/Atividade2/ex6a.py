def click_na_janela(janela_top:int, janela_bottom:int, janela_left:int, janela_right:int, click_x:int, click_y:int) -> bool:
    
    if janela_top <= click_y <= janela_bottom and janela_left <= click_x <= janela_right:
        return True
    else:
        return False

def main():
    #identificar o tamanho da janela
    janela_top : int =  int(input('Informe o top da janela: '))
    janela_bottom : int =  int(input('Informe o bottom da janela: '))
    janela_left : int =  int(input('Informe o left da janela: '))
    janela_right : int =  int(input('Informe o right da janela: '))

    #onde foi feito o click na janela
    click_x : int =  int(input('Informe o click x: '))
    click_y : int =  int(input('Informe o click y: '))

    if click_na_janela(janela_top, janela_bottom, janela_left, janela_right, click_x, click_y):
        print('Click na janela')
    else:
        print('Click fora da janela')

main()
