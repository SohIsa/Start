from aula import Fila
def main():
    filaTeste = Fila()
    filaTeste.inserirDado('IFPB')
    filaTeste.inserirDado('ED')
    filaTeste.inserirDado('2019.2')
    filaTeste.inserirDado('João Pessoa')
    filaTeste.inserirDado('Estágio 1')
    print(filaTeste.getFila())
    filaTeste.remove('2019.2')
    print(filaTeste.getFila())
    print(filaTeste.tamanhoFila())
main()
