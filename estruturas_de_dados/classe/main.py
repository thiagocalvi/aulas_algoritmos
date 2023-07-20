class stack:
    global pilha
    pilha = []
    def add(item):
        pilha[len(pilha)+1] = item
        return pilha
