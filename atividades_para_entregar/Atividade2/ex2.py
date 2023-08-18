from dataclasses import dataclass
"""
    Receber os dados de um aluno e armazená-los em
    uma estrutura de dados, depois imprimir essa 
    estrutura
    Entradas: ra(inteiro), nome(string), curso(string)
    Saída: estrutura com os dados do aluno
"""
@dataclass
class Aluno:
    ra : int
    nome : str
    curso : str

def cadastrarDados(ra:int, nome:str, curso:str):
    """
        Cadastra os dados do aluno na estrutura de 
        dados e retorna essa estrutura
        >>> cadastrarDados(123456, 'Pedro', 'Informatica')
        Aluno(ra=123456, nome='Pedro', curso='Informatica')

        >>> cadastrarDados(654321, 'João', 'Computação')
        Aluno(ra=654321, nome='João', curso='Computação')
        
    """
    aluno = Aluno(ra, nome, curso)
    return aluno

def imprimirDados(aluno:Aluno):
    """
        Impremo os dados armazenados na estrutura de dados Aluno
        >>> imprimirDados(Aluno(123456, 'Pedro', 'Informatica'))
        RA : 123456
        Nome : Pedro
        Curso : Informatica

    """
    print(f'RA : {aluno.ra}')
    print(f'Nome : {aluno.nome}')
    print(f'Curso : {aluno.curso}')

def recebeDados():
    """
        Recebe os dados do aluno e passa para função cadastrarDados e chama
        a função imprimirDados
    """
    ra = int(input("RA do aluno: "))
    nome = input("Nome do aluno: ")
    curso = input("Nome do curso: ")

    dadosAluno = cadastrarDados(ra, nome, curso)
    imprimirDados(dadosAluno)


recebeDados()

