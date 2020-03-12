class Fila:
    def __init__(self):
        self.dados=[]
    def getFila(self):
        return self.dados
    def inserirDado (self,novoValor):
       return self.dados.append(novoValor)
    def removerDado(self):
        return self.dados.pop(0)
    def adeusCarro(self,valor):
        qtde= self.dados.index(valor)
        for i in range(qtde):
            if self.dados[i] != valor:
                self.dados.append(self.dados[i])
        for i in range(qtde+1):
            self.dados.pop(0)
    def tamanhoFila(self):
        return len(self.dados)
