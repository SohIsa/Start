from listaa import Pilha
from fili import Fila
def main ():
    fome = Pilha()
    emof = Fila()
    for i in range(3):
        a=(input('alimento:'))
        fome.push(a)
        emof.novoValor(a)
    print (fome.getPilha())
    print (fome.inverte())
    print (emof.getFila())
    print (emof.verso())

main()
