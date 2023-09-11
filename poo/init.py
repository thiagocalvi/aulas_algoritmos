#Trabalhando com programação orientada a objetos
from dataclasses import dataclass

@dataclass
#instamciando um novo dataclass (estrutura de dados)
class Pessoa:
    name:str = " "
    age:int = 0

    _saldo:float = 0.00



    def get_name(self):
        print(self.name)

    def get_saldo(self):
        print(self._saldo)

    def add_name(self, name:str):
        self.name:str = name
    
    def add_age(self, age:int):
        self.age:int = age 

#definindo uma nova instancia do objeto Pessoa
pessoa1:Pessoa = Pessoa()
pessoa1.name:str = "X"
pessoa1.age:int = 20
pessoa1._saldo = 1000.00

pessoa1.get_name()
pessoa1.add_name("M")
pessoa1.get_name()
pessoa1.get_saldo()


