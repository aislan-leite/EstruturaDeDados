class No:
    def __init__(self, dado  = None, anterior = None, proximo = None):
        self._dado = dado
        self._anterior = anterior
        self._proximo = proximo

    def getAnterior(self):
        return self._anterior
    def setAnterior(self, novoAnterior):
        self._anterior = novoAnterior

    def getProximo(self):
        return self._proximo
    def setProximo(self, novoProximo):
        self._proximo = novoProximo

    def getDado(self):
        return self._dado
    def setDado(self, novoDado):
        self._dado = novoDado

    def __str__(self):
        return str(self.getDado())


class Lista(No):
    def __init__(self, inicio = None, fim = None):
        self._inicio = inicio
        self._fim = fim

    def vazia(self): #Se o início é none então a lista está vazia
        return self._inicio is None

    def buscar(self, valor):
        if self.vazia() == True:
            return None
        i = self._inicio #definir o inicio
        while i != None: #enquanto tiver elemento
            if i.getDado() == valor: #se encontrar
                return i
            i = i.getProximo() #senão passa pro próximo elemento
        return None

    def inserir(self, valor):
        novoNo = No(valor)
        if self.vazia() == True:
            self._inicio = novoNo
            self._fim = novoNo
        else: #insere no meio
            novoNo.setProximo(self._inicio)#novoNo como anterior ao início
            self._inicio.setAnterior(novoNo)
            self._inicio = novoNo

    def inserirFinal(self, valor):
        novoNo = No(valor)
        if self.vazia() == True:
            self._inicio = novoNo
            self._fim = novoNo
        else:
            self._fim.setProximo(novoNo)
            novoNo.setAnterior(self._fim)
            self._fim = novoNo

    def remover(self, valor):
        x = self.buscar(valor)
        if x == None:
            return -1
        if self._inicio != self._fim: #mais de 1 elemento
            if x == self._inicio:
                p = self._inicio.getProximo()
                p.setAnterior(None)
                self._inicio = p
            elif x == self._fim:
                a =  self._fim.getAnterior()
                a.setProximo(None)
                self._fim = a
            else:
                a = x.getAnterior()
                p = x.getProximo()
                p.setAnterior(a)
                a.setProximo(p)
        else:
            self._inicio = None
            self._fim = None

    def exibir(self):
        if self.vazia() is True:
            return self.resul is None
        a = self._inicio

        while a != None:  # enquanto tiver elemento
            print(a)
            a = a.getProximo()  # senão passa pro próximo elemento
            self.resul.append(a)



no = No()
lista = Lista()


lista.inserir(1)
lista.inserir(2)
lista.inserir(3)
print(lista.exibir())
lista.remover(2)
print(lista.exibir())
