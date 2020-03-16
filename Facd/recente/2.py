from listaa import Pilha
from fili import Fila
def main ():
    fome = Pilha()
    grandfome = Pilha()
    emof = Fila()
    fome.push('azul')
    fome.push('rosa')
    fome.push('roxo')
    '''for i in range(3):
        a=(input('alimento:'))
        fome.push(a)
        emof.novoValor(a)'''
    while fome.getPilha():
        grandfome.push(fome.pop())
    print (grandfome.getPilha())
    while grandfome.getPilha():
        emof.novoValor(grandfome.pop())
    print (emof.getFila())

    '''print (fome.getPilha())
    print (fome.inverte())
    print (emof.getFila())
    print (emof.verso())'''

main()
