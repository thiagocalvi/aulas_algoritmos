

def melhores():
    funcionarios:list = ["PEDRO","JOÃO","PEDRO","MARCELO","PEDRO","PEDRO","PEDRO"]
    lucro:list = [300,200,100,450,100,100,100]
    lucros:list = []

    for i in range(len(funcionarios)):
        total = 0
        for j in range(len(funcionarios)):
            if funcionarios[i] == funcionarios[j] and funcionarios[i] not in lucros:
                total += lucro[j]
        
        lucros.append(funcionarios[i])
        lucros.append(total)

    return lucros


lucros = melhores()
print(melhores)


def lucroTotal(lucros):
    totalizado = 0
    for x in range(len(lucros)):
        if x % 2 != 0:
            totalizado += lucros[x]

    print(totalizado)


lucroTotal(lucros)