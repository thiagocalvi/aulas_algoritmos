#F para C > (F - 32) * 5/9
#se C < 17 "FRIO"
#C > 25 "CALOR"
#C entre 17 e 25 "AGRADAVEL"


temperaturaF = input("Informe a temperatura em F°")

def converteParaC(temp: int):
    temperaturaC = (int(temp) - 32) * (5/9)
    return round(temperaturaC)

temperaturaC = converteParaC(int(temperaturaF))

print(temperaturaC)

if temperaturaC < 17:
    print("FRIO")
elif temperaturaC > 25:
    print("CALOR")
else:
    print("AGRADAVEL")

