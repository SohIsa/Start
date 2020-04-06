class Pilha:
    def __init__(self):
        self.__dados = []
    def getPilha(self):
        return self.__dados
    def push (self,novoValor):
        return self.__dados.append(novoValor)
    def topo(self):
        return (self.__dados[len(self.__dados)-1])
    def backspace(self):
        return self.__dados.pop()
    def esvaziar (self):
        while (len(self.__dados)!=0):
            self.__dados.pop()
    def tamanhoPilha(self):
        return len(self.__dados)
    def inverte(self):
        pilhaN = []
        for i in range(len(self.__dados)):
            b = self.__dados.pop()
            pilhaN.append(b)
        return pilhaN
