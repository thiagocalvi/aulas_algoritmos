from dataclasses import dataclass

@dataclass
class Estoque:
    q_bobinas:int = 100000
    q_chapas:int = 50000
    q_paineis:int = 30000