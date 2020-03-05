class Fila:
    def __init__(self):
        self.dados=[]
    def getFila(self):
        return self.dados
    def inserirDado (self,novoValor):
       return self.dados.append(novoValor)
    def removerDado(self):
        return self.dados.pop(0)
    def remove(self,valor):
        pos = self.dados.index(valor)
        for i in range(0,pos+1):
            #self.dados.pop(0)
            self.removerDado()
    def tamanhoFila(self):
        return len(self.dados)
