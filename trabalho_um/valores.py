from dataclasses import dataclass

@dataclass
class Valores:
	valor_custo_bobina:float = 50.00
	valor_custo_chapa:float = 40.00 
	valor_custo_painel:float = 75.00 
	
	valor_venda_bobina:float = 60.00 
	valor_venda_chapa:float = 48.00 
	valor_venda_painel:float = 90.00 