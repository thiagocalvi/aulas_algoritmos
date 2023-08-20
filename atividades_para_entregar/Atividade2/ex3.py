from dataclasses import dataclass
"""
    Receber um intervalo de tempo em minutos e 
    converter para uma estrutura contendo horas
    e minutos equivalentes
    Entradas: intervalo em minutos(inteiro)
    Saída: estrutura composta contendo os campos
    horas e minutos
"""
@dataclass
class Tempo:
    horas : int
    minutos : int

def converterTempo(minutos : int) -> Tempo:
    """
        Recebe o intervalo em minutos e converte para
        horas e minutos
        >>> converterTempo(131)
        Tempo(horas=2, minutos=11)

        >>> converterTempo(254)
        Tempo(horas=4, minutos=14)
    """

    tempo = Tempo(0,0)
    tempo.horas : int = minutos // 60
    tempo.minutos : int = minutos % 60

    return tempo


def main():
    minutos = int(input('Informe o intervalo em minutos: '))
    tConvertido : Tempo = converterTempo(minutos)
    print(f'Horas: {tConvertido.horas}')
    print(f'Minutos: {tConvertido.minutos}')

main()