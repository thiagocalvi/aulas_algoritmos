#tempo de viagem: input
#velocidade: input
#distancia percorida: ?
#autonomia: 12Km/L
#formula: (tempo de viagem * velocidade) / autonomia 

tempoViagem = input("Informe o tempo gasto na viagem: ")
velocidadeMedia = input("Informe a velocidade média da viagem: ")

def distanciaPercorida(tempoViagem: int, velocidadeMedia: int) -> int:
    distancia = int(tempoViagem) * int(velocidadeMedia)
    return distancia

combustivelGasto = distanciaPercorida(tempoViagem, velocidadeMedia) / 12

print("Consumo" + combustivelGasto + "L")