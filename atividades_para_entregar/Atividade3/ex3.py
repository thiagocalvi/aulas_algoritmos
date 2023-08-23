from enum import Enum, auto

class Voto(Enum):
    
    CANDIDATO1 = auto()
    CANDIDATO2 = auto()
    VOTOBRANCO = auto()

def contaVotos(listaVotos:list):
    """
        Quando for passar os parametros passar entre asapas senão essa merda não funciona!
    """
    q_cand1 = 0
    q_cand2 = 0
    q_branco = 0
    
    for x in range(len(listaVotos)):
        
        if listaVotos[x] == Voto.CANDIDATO1.name:
            q_cand1 += 1
        elif listaVotos[x] == Voto.CANDIDATO2.name:
            q_cand2 += 1
        else: 
            q_branco += 1

    return q_cand1, q_cand2, q_branco


def verifica(q_cand1, q_cand2, q_branco):
    if q_branco > q_cand1 + q_cand2:
        print("Novas eleições")
    else:
        if q_cand1 > q_cand2:
            print("Vencerdor candidato 1")
        else:
            print("Vencerdor candidato 2")
