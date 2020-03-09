from aula import Pilha
def main():
    pilhaTeste=Pilha()
    '''for i in range (5):
        pilhaTeste.push(input('nome:'))'''
    nome = input('nome:').split()
    for i in nome:
        pilhaTeste.push(i)
    print(pilhaTeste.getPilha())
    pilhaTeste.pop()
    print(pilhaTeste.getPilha())
    pilhaTeste.esvaziar()
    print(pilhaTeste.getPilha())
main()
