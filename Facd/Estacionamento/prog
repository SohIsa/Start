from aula import Fila
def main():
    estacionamento= Fila()
    vagas=(int(input('quantas vagas no estacionamento?')))
    while estacionamento.tamanhoFila() < vagas:
        desejo=(input('(A) para entrar ou (B) para sair:'))
        if desejo == ('A') or desejo == ('a'):
           estacionamento.inserirDado(input('placa:'))
           print (estacionamento.getFila())
        elif desejo == ('B') or desejo == ('b'):
            estacionamento.adeusCarro(input('qual sai?'))
            print(estacionamento.getFila())
       
   

main()
