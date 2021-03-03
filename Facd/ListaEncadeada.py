class No:
  def __init__(self,carga: object = None, prox: 'No' = None):
    self.carga = carga
    self.prox = prox

  def __str__(self):
    return str(self.carga)

class ListaEncadeada:
  def __init__(self):
    self.cabeca = None
    self.cauda = None

  def imprimir (self):
    if self.cabeca is None:
      print ('Lista vazia')
    atual: 'No' = self.cabeca
    while atual is not None:
      print (str(atual.carga)) #tentar aqui
      atual = atual.prox

  def inserir_inicio(self, valor: object):
    novo: "No" = No(valor)
    if self.cabeca is None:
      self.cabeca = self.cauda = novo
    else:
      novo.prox = self.cabeca
      self.cabeca = novo

  def inserir_fim(self, valor: object):
    novo = No(valor)
    if self.cabeca is None:
      self.cabeca = self.cauda = novo
    else:
      self.cauda.prox = novo
      self.cauda = novo
  
  '''def juntar(listaa,listab):
    listax= ListaEncadeada()
    listax=listaa
    atual:'No' = listab.cabeca
    while atual.prox is not None:
      listax.inserir_fim(atual)
      atual = atual.prox
    return listax'''
    
 
listaa = ListaEncadeada()
listab = ListaEncadeada()
listac = ListaEncadeada()
listaa.inserir_inicio(1)
listaa.inserir_fim(7)
listaa.imprimir()
print ('#######################')
listab.inserir_inicio(3)
listab.inserir_fim(4)
listab.inserir_fim(8)
listab.imprimir()
print ('#######################')
listac = listaa
atual = listab.cabeca
while atual.prox is not None:
  listac.inserir_fim(atual)
  atual = atual.prox
listac.imprimir()
