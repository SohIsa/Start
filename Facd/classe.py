class Pilha:
    def __init__(self):
        self.__dados = []
    def getPilha(self):
        return self.__dados
    #def inserirDado(self, novoValor):
    #pop e push é coisa de pilha
    def push(self, novoValor):
        self.__dados.append(novoValor)
    #def removerDado(self):
    def pop(self):
        self.__dados.pop()
    #def topo(self):

    def esvaziar(self):
        while (len(self.__dados)!=0):
            self.__dados.pop()
