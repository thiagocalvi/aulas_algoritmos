#calcular area das paredes e do teto 
#calcular a quantidade de latas para pintar a area total, teto + paredes

IalturaParedeMa = input('Altura da parede Maior: ')
IlarguraParedeMa = input('Largura da parede Maior: ')
IlarguraParedeMe = input('Largura da parede Menor: ')

larguraParedeMa = int(IlarguraParedeMa)
larguraParedeMe = int(IlarguraParedeMe)
alturaParedeMa = int(IalturaParedeMa)


areaParedeMa = alturaParedeMa * larguraParedeMa
areaParedeMe = alturaParedeMa * larguraParedeMe
areaTeto = larguraParedeMe * larguraParedeMa

areaTotal = (areaParedeMa * 2) + (areaParedeMe * 2) + areaTeto

quantidadeLatas = areaTotal / 12

print(areaTotal)
print( quantidadeLatas)