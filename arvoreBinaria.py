class No:
    def __init__(self, dado):
        self._dado = dado
        self._filhoEsquerda = None
        self._filhoDireita = None
        self._pai = None

    def getDado(self):
        return self._dado
    def setDado(self, valorNovo):
        self._dado = valorNovo

    def getFilhoEsquerda(self):
        return self._filhoEsquerda
    def setFilhoEsquerda(self, valorNovo):
        self._filhoEsquerda = valorNovo

    def getFilhoDireita(self):
        return self._filhoDireita
    def setFilhoDireta(self, valorNovo):
        self._filhoDireita = valorNovo

    def getPai(self):
        return self._pai
    def setPai(self, valorNovo):
        self._pai = valorNovo

    def __str__(self):
        return str(" no: " + str(self.getDado()))

class ArvoreBinaria(No):
    def __init__(self):
        self._raiz = None #unica diferença de um nó  e uma árvore é a raiz

    def getRaiz(self):
        return self._raiz
    def setRaiz(self, novoValor):
        self._raiz = novoValor

    def buscar(self, raiz, dado):
        if raiz == None or raiz.getDado() == dado:
            return raiz

        if dado < raiz.getDado():
            return self.buscar(raiz.getFilhoEsquerda(), dado)

        else:
            return self.buscar(raiz.getFilhoDireita(), dado)

    def minimo(self, raiz):
        while raiz.getFilhoEsquerda() is not None:
            raiz = raiz.getFilhoEsquerda()
        return raiz

    def maximo(self):
        while raiz.getFilhoDireita() is not None:
            raiz = raiz.getFilhoDireita()
        return raiz

    def sucessor(self, raiz):
        if raiz.getFilhoDireita() != None:
            return self.minimo(raiz.getFilhoDireita)

        paiRaiz = raiz.getPai()
        while paiRaiz != None and raiz is paiRaiz.getFilhoDireita():
            raiz = paiRaiz
            paiRaiz = paiRaiz.getPai();

        return paiRaiz

    def predecessor(self, raiz):
        if raiz.getFilhoEsquerda() != None:
            return self.maximo(raiz.getFilhoEsquerda)

        paiRaiz = raiz.getPai()
        while paiRaiz != None and raiz is paiRaiz.getFilhoEsquerda():
            raiz = paiRaiz
            paiRaiz = paiRaiz.getPai();

        return paiRaiz

    def inserir(self, valor):
        paiRaiz = None
        raiz = self.getRaiz()
        while raiz != None:
            paiRaiz = raiz
            if valor.getDado() < raiz.getDado():
                raiz = raiz.getFilhoEsquerda()
            else:
                raiz = raiz.getFilhoDireita()

        valor.setDado(paiRaiz)
        if paiRaiz == None: #arvoreVazia
            self.setRaiz(valor)
        else:
            if valor.getDado() < paiRaiz.getDado():
                paiRaiz.setFilhoEsquerda(valor)
            else:
                paiRaiz.setFilhoDireita(valor)


    def remover(self, raiz):
        if raiz.getFilhoEsquerda == None or raiz.getFilhoDireita == None:
            y = raiz
        else:
            y = self.sucessor(raiz)

        if y.getFilhoEsquerda() != None:
            z = y.getFilhoEsquerda()
        else:
            z = y.getFilhoDireita()

        if z != None:
            z.setPai(y.getPai())

        if y.getPai() == None:
            self.setRaiz(z)
        else:
            if y == y.getPai().getFilhoEsquerda():
                y.getPai().setFilhoEsquerda(z)
            else:
                y.getPai().setFilhoDireita(z)

        if y != raiz:
            raiz.setDado(y.getDado())
