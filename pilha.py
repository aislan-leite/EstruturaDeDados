class Pilha:
    def __init__(self):
        self.pilha = []
    def inserir(self, n):
        self.pilha.append(n)
    def tamanho(self):
        return len(self.pilha)
    def excluir(self):
        if not self.vazia():
            del self.pilha[self.tamanho()-1]
    def vazia(self):
        return self.tamanho() == 0
    def exibir(self):
        return self.pilha


pilha = Pilha()
pilha.inserir(39)
pilha.inserir(12)
pilha.inserir(123)
print(pilha.exibir())

print(pilha.vazia())

pilha.excluir()
print(pilha.exibir())
pilha.excluir()
print(pilha.exibir())
