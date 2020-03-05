from aula import Fila
def main():
    estacionamento= Fila()
    despercidio= Fila()
    estacionamento.inserirDado('12')
    estacionamento.inserirDado('5')
    estacionamento.inserirDado('3')
    estacionamento.inserirDado('84')
    print(estacionamento.getFila())
    print(estacionamento.tamanhoFila())
    #placa=input('placa:')
    placa=('5')
    
    estacionamento.remove(placa)
    print(estacionamento.getFila())
    print(estacionamento.tamanhoFila())
main()
