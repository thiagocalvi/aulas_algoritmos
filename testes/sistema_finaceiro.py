from dataclasses import dataclass

@dataclass
class Valores:
	valor_custo_bobina:float = 50.00
	valor_custo_chapa:float = 40.00 
	valor_custo_painel:float = 75.00 
	
	valor_venda_bobina:float = 60.00 
	valor_venda_chapa:float = 48.00 
	valor_venda_painel:float = 90.00 

valores:Valores = Valores()


notas = [{'vendedor': 'João', 'produto': 'BOBINA', 'quantidade': 45, 'valor_desconto': 1222},
{'vendedor': 'Paulo', 'produto': 'CHAPA', 'quantidade': 85, 'valor_desconto': 2000},
{'vendedor': 'Maria', 'produto': 'BOBINA', 'quantidade': 89, 'valor_desconto': 1002}]


#busca todos os vendedores nas notas de vendas
def vendedores(notas:list)->list:
    nome_vendedores:list = []
    #busca os nome dos vendedores e salva em uma lista
    for i in notas:
        if i["vendedor"] not in nome_vendedores: 
            nome_vendedores.append(i["vendedor"])

    return nome_vendedores


#totaliza o valor das vendas de cada vendedor
def total_vendido_por_vendedor(notas:list, vendedores:list)->list:
    total_por_vendedor:list = []
    
    for x in vendedores:
        total_desconto = 0
        total_vendido = 0
        for i in notas:
            if x == i["vendedor"]:
                produto = i["produto"]
                if produto == "BOBINA":
                    total_desconto += i["valor_desconto"]
                    total_vendido += valores.valor_venda_bobina * i["quantidade"]
                elif produto == "CHAPA":
                    total_desconto += i["valor_desconto"]
                    total_vendido += valores.valor_venda_chapa * i["quantidade"]
                elif produto == "PAINEL":
                    total_desconto += i["valor_desconto"]
                    total_vendido += valores.valor_venda_painel * i["quantidade"]

        total_por_vendedor.append({"vendedor":x, "total_vendido":total_vendido - total_desconto})
        

    return total_por_vendedor



#classifica os tres melhores vendedores
def melhores_vendedores(total_por_vendedor:list)->list:  
    lista_vendedores:list = total_por_vendedor 
    melhores:list = []

    while lista_vendedores:
        maior = lista_vendedores[0]
        for vendedor in lista_vendedores:
            if vendedor["total_vendido"] > maior["total_vendido"]:
                maior = vendedor
        
        melhores.append(maior)
        lista_vendedores.remove(maior)

    
    return melhores



