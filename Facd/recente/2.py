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
    #com while eh melhor por agora pq a funcção criada não é generica o que eventualmente pode atrapalhar
    #pop tbm conhecido como backspace caso eu n tenha mudado
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
