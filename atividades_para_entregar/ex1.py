"""
    Ler a senha e verificar se coresponde com a senha do sistema,
    se sim liberar o acesso caso contrario não liberar o acesso

    variaveis:
    
"""

def verificarSenha(senha:str) -> bool:
    """
        Verifica se a senha pasada como parametro corresponde a 
        senha armazenada na variavel senhaCorreta, se forem corespondentes
        retorna True caso contrario retorna False

        >>> verificarSenha('Qualquer123')
        False
        
        >>> verificarSenha('Giva123')
        True
    """
    senhaCorreta : str = 'Giva123'

    if senha == senhaCorreta:
        return True
    else:
        return False


def liberarAcesso():
    
    inputSenha : str = input("Informe a senha de acesso: \n")

    acessoLiberado : bool = verificarSenha(inputSenha)

    if acessoLiberado:
        print("Senha correta, acesso liberado")
    else:
        print("Senha incorreta, acesso negado")


