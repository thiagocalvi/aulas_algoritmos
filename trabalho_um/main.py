from estoque import Estoque
from demanda import Demanda
from valores import Valores
from relatorio_vendas import relatorio_vendas as vendas

estoque:Estoque = Estoque()
demanda:Demanda = Demanda()
valores:Valores = Valores()

pedidos = {
	"BOBINAS" : 150,
	"CHAPAS" : 45,
	"PAINEIS" : 48
    }

def main():
    print("""PAINEL DE CONTROLE
          ----ESCOLHA UMA OPÇÃO----
          [1] - CADASTRAR VENDEDOR
          [2] - CRIAR NOVO PEDIDO
          [3] - RELATÓRIO
          [X] - SAIR""")
    
    opcao_selecionada:str = input("Opção:")

    if opcao_selecionada == "1":
        adicionar_vendedor()
    elif opcao_selecionada == "2":
        criar_novo_pedido()
    elif opcao_selecionada == "3":
        relatorio()
    elif opcao_selecionada == "x" or opcao_selecionada == "X":
        sair()


#função para cadastrar um vendedor 
lista_vendedores:list = []
def adicionar_vendedor():
    print("-----Cadastro de vendedor-----\n")
    
    nome_vendedor:str = input("Informe o nome do vendedor: ")
   
    if nome_vendedor.upper() in lista_vendedores:
        print("Vendedor já está cadastrado")
        
    else:
        lista_vendedores.append(nome_vendedor.upper())
        print(f'{nome_vendedor} cadastrado como vendedor')

    main()



#receber informaçoes do pedidos
def criar_novo_pedido():

    if len(lista_vendedores) == 0:
        print("Não existe vendedores cadastrados! Adicione um vendedor para continuar")
        main()

    print("SELECIONE O VENDEDOR")
    for x in range(len(lista_vendedores)):
        print(f"[{x+1}] - {lista_vendedores[x]}")
    
    index_vendedor:int = int(input("Vendedor: "))

    if index_vendedor-1 < 0 or  index_vendedor-1 > len(lista_vendedores)-1:
        print("Opção invalida")
        criar_novo_pedido()
    
    nome_vendedor:str = lista_vendedores[index_vendedor-1] 

    print("""SELECIONE O PRODUTO
          [1] - BOBINAS
          [2] - CHAPAS
          [3] - PAINEIS""")

    nome_produto:str = input("Produto: ")

    if nome_produto == "1":
        nome_produto = "BOBINAS"
    elif nome_produto == "2":
        nome_produto = "CHAPAS"
    elif nome_produto == "3":
        nome_produto = "PAINEIS"
    else:
        print("Opção invalida")
        criar_novo_pedido()
    
    quantidade_produto:int = int(input("Qauntidade: "))
    
    if quantidade_produto <= 0:
        print("Qauntidade não pode ser manor ou igual a zero")
        criar_novo_pedido()    

    #recebe o valor total desconto
    valor_desconto:float = float(input("Informe o valor do desconto: "))

    #verificar se quantidade de desconto oferecida é menor que valor total de custo
    if nome_produto == "BOBINAS":
        if (valores.valor_custo_bobina * quantidade_produto) < valor_desconto:
            print("Valor do desconto muito alto")
            criar_novo_pedido()    

    elif nome_produto == "CHAPAS":
        if (valores.valor_custo_chapa * quantidade_produto) < valor_desconto:
            print("Valor do desconto muito alto")
            criar_novo_pedido()    

    elif nome_produto == "PAINEIS":
        if (valores.valor_custo_painel * quantidade_produto) < valor_desconto:
            print("Valor do desconto muito alto")
            criar_novo_pedido()    
    else:
        vendas.append({"vendedor": nome_vendedor, "produto": nome_produto, "quantidade" : quantidade_produto,"valor_desconto": valor_desconto})



#totaliza os pedidos
def totalizar_pedidos(pedidos, demanda:Demanda)->Demanda:
 
    for produto in pedidos:

        if produto == "BOBINAS":
            demanda.d_bobinas += pedidos["BOBINAS"]
        elif produto == "CHAPAS":
            demanda.d_chapas += pedidos["CHAPAS"]
        elif produto == "PAINEIS":
            demanda.d_paineis += pedidos["PAINEIS"]

    return demanda


#verifica se existe rupturas
def ha_rupturas(demanda:Demanda, estoque:Estoque):
    rupturas = {}

    if demanda.d_bobinas > estoque.q_bobinas:
        rupturas["BOBINAS"] = "Bobinas em falta"
    elif demanda.d_chapas > estoque.q_chapas:
        rupturas["CHAPAS"] = "Chapas em falta"
    elif demanda.d_paineis > estoque.q_paineis:
        rupturas["PAINEIS"] = "Paineis em falta"

    if len(rupturas) == 0:
        return False
    
    return rupturas

#FIM SISTEMA ESTOQUE

#INICIO SISTEMA VENDAS

#função para classificar os 3 melhores vendedores
# vendas = {
# 	"A001": {"vendedor": "João", "produto":"BOBINA", "quantidade" : 45,"valor_desconto": 1222},
# 	"A002": {"vendedor": "Paulo", "produto":"CHAPAS", "quantidade" : 85,"valor_desconto": 2000},
# 	"A003": {"vendedor": "João", "produto":"BOBINA", "quantidade" : 89,"valor_desconto": 1002}
# }

def melhores_vendedores(vendas):
    vendedores:list = []
    #buscar todos os vendedores
    for x in vendas:
        if vendas[x]["vendedor"] not in vendedores:
            vendedores.append(vendas[x]["vendedor"])

    #contabilizar o total de venda de cada vendedor

    

melhores_vendedores(vendas)


def total_descontos(vendas):
    descontos = 0
    for x in vendas:
        descontos += vendas[x]["desconto"]
    
    return descontos
        
        

def lucro_liquido(vendas, valores:Valores):
    
    lucro = 0
    deconto = total_descontos(vendas)

    for x in vendas:
        if vendas[x]["produto"] == "BIBINA":
            lucro += vendas[x]["quantidade"] * valores.valor_venda_bobina

        elif vendas[x]["produto"] == "CHAPA":
            lucro += vendas[x]["quantidade"] * valores.valor_venda_chapa

        elif vendas[x]["produto"] == "PAINEL":
            lucro += vendas[x]["quantidade"] * valores.valor_venda_painel


    return lucro - deconto



#retorna os relatios com as notas de vendas
def relatorio():
    print("mostra o relatorio")