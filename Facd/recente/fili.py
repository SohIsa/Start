class Fila:
    def __init__(self):
        self.__dados=[]
    def getFila (self):
        return self.__dados
    def novoValor(self, novoValor):
        return self.__dados.append(novoValor)
    def remocerdado(self):
        return self.__dados.pop()
    def verso(self):
        filete=[]
        for i in range(len(self.__dados)):
            a=self.__dados.pop(0)
            filete.append(a)
        return a
