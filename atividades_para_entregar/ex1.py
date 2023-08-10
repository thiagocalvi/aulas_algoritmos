def verificarSenha(senha:str) -> bool:
    """
        Verifica se a senha pasada como parametro corresponde a 
        senha armazenada na variavel senhaCorreta, se forem correspondentes
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

liberarAcesso()
