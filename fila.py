class Fila:
    def __init__(self):
        self.fila = []
    def inserir(self,n):
        self.fila.append(n)
    def excluir(self):
        if not self.vazia():
            del self.fila[0]
    def tamanho(self):
        return len(self.fila)
    def vazia(self):
        return self.tamanho() == 0
    def exibir(self):
        return self.fila

fila = Fila()
fila.inserir(1)
fila.inserir(50)
fila.inserir(145)
fila.inserir(45585)

print(fila.exibir())

fila.excluir()

print(fila.exibir())

fila.excluir()

print(fila.exibir())

fila.excluir()

print(fila.exibir())

