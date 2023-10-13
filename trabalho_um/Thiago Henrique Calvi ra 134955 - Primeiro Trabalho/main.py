from estruturas_dados.estoque import Estoque
from estruturas_dados.demanda import Demanda
from estruturas_dados.valores import Valores


estoque:Estoque = Estoque()
demanda:Demanda = Demanda()
valores:Valores = Valores()

vendas:list = []

#recebe do usuario as informações de uma venda e cadastra em vendas
def cadastar_pedido():
    """
    Recebe as informações de um pedido que são pasadas pelo usuario, e salva o pedido em vendas
    Entradas: nome_vendedor:str, nome_produto:str, quantidade_produto:int, valor_desconto:float
    Saida: sem saida
    """
    #recebe o nome do vendedor
    nome_vendedor:str = input("Informe o nome do vendedor: ")

    #vrifica se o nome do vendedor é vazio
    if nome_vendedor == " ":
        print("Informe o nome de um vendedor!")
        main() 

    #tabela para selecionar o produto
    print("""SELECIONE O PRODUTO
          [1] - BOBINAS
          [2] - CHAPAS
          [3] - PAINEIS""")

    #recebe o numero correspondente ao produto
    nome_produto:str = input("Produto: ")

    #verifica qual produto foi selecionado
    if nome_produto == "1":
        nome_produto = "BOBINAS"
    elif nome_produto == "2":
        nome_produto = "CHAPAS"
    elif nome_produto == "3":
        nome_produto = "PAINEIS"
    else:
        print("Opção invalida, escolhar uma das opções do painel")
        main()
    
    #recebe a quantidade do produto
    quantidade_produto:int = int(input("Qauntidade do produto: "))
    
    #verifica se a quantidade do produto é menor o igual a zero
    if quantidade_produto <= 0:
        print("Qauntidade não pode ser manor ou igual a zero")
        main()

    #recebe o valor do desconto oferecido
    valor_desconto:float = float(input("Informe o valor do desconto em reias: "))

    #verificar se o valor de desconto oferecida é menor que o valor total de custo de produção do produto
    if nome_produto == "BOBINAS":
        if (valores.valor_custo_bobina * quantidade_produto) >= (valores.valor_venda_bobina * quantidade_produto) - valor_desconto:
            print("Valor do desconto muito alto")
            main()    

    elif nome_produto == "CHAPAS":
        if (valores.valor_custo_chapa * quantidade_produto) >= (valores.valor_venda_chapa * quantidade_produto) - valor_desconto:
            print("Valor do desconto muito alto")
            main()    

    elif nome_produto == "PAINEIS":
        if (valores.valor_custo_painel * quantidade_produto) >= (valores.valor_venda_painel * quantidade_produto) - valor_desconto:
            print("Valor do desconto muito alto")
            main()    

    #cadastra a venda na estrutura de vendas
    vendas.append({"vendedor": nome_vendedor.upper(), "produto": nome_produto, "quantidade" : quantidade_produto,"valor_desconto": valor_desconto})
    
#totaliza a quantidae de pedidos e salva na estrutura de demanda e retorna essa estrutura
def totalizar_pedidos(vendas:list, demanda:Demanda)->Demanda:
    """
    totaliza a quantidade de produtos nos pedidos feito, salva na estrutura Demanda e retorna essa estrutura
    Entradas: vendas:list, demanda:Demanda
    Saida: demanda:Demanda
    >>> demanda = Demanda()
    >>> totalizar_pedidos([{"vendedor": "PEDRO", "produto": "BOBINAS", "quantidade": 10, "valor_desconto": 5.0}], demanda)
    Demanda(d_bobinas=10, d_chapas=0, d_paineis=0)
    """
    for produto in vendas:

        if produto["produto"] == "BOBINAS":
            demanda.d_bobinas += produto["quantidade"]
        elif produto["produto"] == "CHAPAS":
            demanda.d_chapas += produto["quantidade"]
        elif produto["produto"] == "PAINEIS":
            demanda.d_paineis += produto["quantidade"]

    return demanda

#verifica se existe rupturas
def ha_rupturas(demanda:Demanda, estoque:Estoque):
    """
    Baseado nas estruturas de demanda e estoque, verifica se existe rupturas.

    Args:
        demanda (Demanda): Estrutura de demanda.
        estoque (Estoque): Estrutura de estoque.

    Returns:
        dict or bool: Um dicionário de rupturas se houver rupturas, caso contrário, False.

    Exemplos:
    >>> ha_rupturas(Demanda(d_bobinas=180, d_chapas=200, d_paineis=300), Estoque(q_bobinas=150, q_chapas=250, q_paineis=350))
    {'BOBINAS': 'Bobinas em falta'}
    >>> ha_rupturas(Demanda(d_bobinas=100, d_chapas=200, d_paineis=300), Estoque(q_bobinas=150, q_chapas=250, q_paineis=400))
    False
    """
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

#busca todos os vendedores nas notas de vendas e retorna uma lista com os nomes
def vendedores(vendas:list)->list:
    """
    Busca e salva em uma lista o nome dos vendedores que estão na lista vendas.

    Args:
        vendas (list): Lista de vendas.

    Returns:
        list: Lista de nomes de vendedores.

    Exemplos:
    >>> vendas = [{'vendedor': 'PAULO', 'total_vendido': 132920.0},
    ...           {'vendedor': 'PEDRO', 'total_vendido': 119900.0}]
    >>> vendedores(vendas)
    ['PAULO', 'PEDRO']
    """
    nome_vendedores:list = []
    #busca os nome dos vendedores e salva em uma lista e retorna essa lista
    for i in vendas:
        if i["vendedor"] not in nome_vendedores:
            nome_vendedores.append(i["vendedor"])

    return nome_vendedores

#totaliza o valor das vendas de cada vendedor
def total_vendido_por_vendedor(vendas:dict, vendedores:list)->dict:
    """
    Totaliza o valor das vendas de cada vendedor.

    Args:
        vendas (list): Lista de vendas.
        vendedores (list): Lista de vendedores.

    Returns:
        list: Lista de dicionários contendo o nome do vendedor e o valor total vendido.

    Exemplos:
    >>> vendas = [{'vendedor': 'PEDRO', 'produto': 'BOBINAS', 'quantidade': 10, 'valor_desconto': 5.0},
    ...           {'vendedor': 'MARIA', 'produto': 'CHAPAS', 'quantidade': 20, 'valor_desconto': 10.0}]
    >>> vendedores = ['PEDRO', 'MARIA']
    >>> total_vendido_por_vendedor(vendas, vendedores)
    [{'vendedor': 'PEDRO', 'total_vendido': 595.0}, {'vendedor': 'MARIA', 'total_vendido': 950.0}]
    """

    total_por_vendedor:list = []
    
    for x in vendedores:
        total_desconto:float = 0
        total_vendido:float = 0
        for i in vendas:
            if x == i["vendedor"]:
                produto:str = i["produto"]
                if produto == "BOBINAS":
                    total_desconto += i["valor_desconto"]
                    total_vendido += valores.valor_venda_bobina * i["quantidade"]
                elif produto == "CHAPAS":
                    total_desconto += i["valor_desconto"]
                    total_vendido += valores.valor_venda_chapa * i["quantidade"]
                elif produto == "PAINEIS":
                    total_desconto += i["valor_desconto"]
                    total_vendido += valores.valor_venda_painel * i["quantidade"]

        total_por_vendedor.append({"vendedor":x, "total_vendido":total_vendido - total_desconto})
        

    return total_por_vendedor

#classifica os melhores vendedores do maior valor vendido para o menor valor vendido
def melhores_vendedores(total_por_vendedor:dict)->dict:  
    """
    Classifica os 3 melhores vendedores do maior valor vendido para o menor valor vendido.

    Args:
        total_por_vendedor (dict): Dicionário contendo informações de vendas por vendedor.

    Returns:
        list: Lista de vendedores ordenados por valor vendido.

    Exemplos:
    >>> melhores_vendedores([{'vendedor': 'PEDRO', 'total_vendido': 95.0}, {'vendedor': 'MARIA', 'total_vendido': 190.0}, {'vendedor': 'MARCOS', 'total_vendido': 160.0}])
    [{'vendedor': 'MARIA', 'total_vendido': 190.0}, {'vendedor': 'MARCOS', 'total_vendido': 160.0}, {'vendedor': 'PEDRO', 'total_vendido': 95.0}]
    """
    
    lista_vendedores:list = total_por_vendedor 
    melhores:list = []

    while lista_vendedores:
        maior:dict = lista_vendedores[0]
        for vendedor in lista_vendedores:
            if vendedor["total_vendido"] > maior["total_vendido"]:
                maior = vendedor
        
        melhores.append(maior)
        lista_vendedores.remove(maior)

    
    return melhores

#calcula o lucro liquido da empresa
def lucro_liquido(total_por_vendedor:dict)->float:
    """
    Calcula o lucro líquido da empresa.

    Args:
        total_por_vendedor (dict): Dicionário contendo informações de vendas por vendedor.

    Returns:
        float: O lucro líquido da empresa.

    Exemplos:
    >>> lucro_liquido([{'vendedor': 'PEDRO', 'total_vendido': 95.0}, {'vendedor': 'MARIA', 'total_vendido': 190.0}])
    'Lucro de R$285.0'
    """

    c_bobinas:int = demanda.d_bobinas * valores.valor_custo_bobina
    c_chapas:int= demanda.d_chapas * valores.valor_custo_chapa
    c_paineis:int = demanda.d_paineis * valores.valor_custo_painel

    custo_producao_total:int = c_bobinas + c_chapas + c_paineis

    total_vendido:int = 0

    for venda in total_por_vendedor:
        total_vendido += venda["total_vendido"]
    

    lucro_total = total_vendido - custo_producao_total

    situacao:str = "Lucro de R$"

    if lucro_total < 0.0:
        situacao = "Prejuizo de R$ "

    return situacao + str(lucro_total)

#gera o relatorio printa na tela as vendas realizadas, lucro liquido e os melhores vendedores
def relatorio(total_por_vendedor:dict):
    """
    Gera o relatório, imprime na tela as vendas realizadas, lucro líquido e os melhores vendedores.
    Entrada: total_por_vendedor: dict
    Saída: sem retorno
    """

    lucro:str = lucro_liquido(total_por_vendedor)
    
    melhores:dict = melhores_vendedores(total_por_vendedor)
    tres_melhores:dict =  melhores[:3]
    
    rupturas = ha_rupturas(demanda,estoque)

    if rupturas == False:
        print("Sem rupturas")
    else:
        for x in rupturas:
            print(x)

    print(f'Vendas realizadas: {vendas}')

    print(f'Melhores vendedores:')
    n:int = 1
    for x in tres_melhores:
        total_vendido:float = x["total_vendido"]

        print(f'{n} - {x["vendedor"]} - Valor vendido : R$ {total_vendido}')
        n += 1
    print(lucro)

#finaliza o programa
def sair():
    exit()

#inicia o programa
def main():
    print("""PAINEL DE CONTROLE
          ----ESCOLHA UMA OPÇÃO----
          [1] - CRIAR NOVO PEDIDO
          [2] - RELATÓRIO
          [X] - SAIR""")
    
    opcao_selecionada:str = input("Opção selecionada:")

    #chama uma determinada função dependendo da escolha do usuario
    if opcao_selecionada == "1":
        cadastar_pedido()
        totalizar_pedidos(vendas,demanda)
        main()
    elif opcao_selecionada == "2":
        vendedor = vendedores(vendas)
        total_vend = total_vendido_por_vendedor(vendas, vendedor)
        relatorio(total_vend)
        main()
    elif opcao_selecionada == "x" or opcao_selecionada == "X":
        sair()
    else:
        print("Opção invalida")
        main()

#main()
