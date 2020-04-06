#começando pelo 004 (dissecando uma variável)
'''def main():
    palavra = input('digite:')
    print (f'o tipo primitivo desse valor {type(palavra)}')
    print ('Só tem espaço?', palavra.isspace())
    print('é um número?', palavra.isnumeric())
    print('é alfabético?',palavra.isalpha())
    print('alfanumerico?',palavra.isalnum())
    print('minusculo?', palavra.islower())
    print('maiusculo?', palavra.isupper())
    print('está capitalizada?',palavra.istitle())
main()'''
#005 antecessor e sucessor
'''def main():
    valor=int(input('digite um número:'))
    print( f'seu antecessor é {valor-1} e o seu sucessor é {valor+1}')
main()'''
#006 dobro, triplo e raiz quadrada
'''def main():
    valor=int(input('digite um número:'))
    print(f'o dobro de {valor} é {valor*2} e a raiz é {valor**(1/2)}')
main()'''
#008 conversor de medidas
def conv(valor):
    return (f'{valor/1000}km, {valor/100}hm, {valor/10}dam, {valor*100}cm, {valor*1000}mm')
'''def main():
    num=int(input('digite um valor em metros:'))
    print(conv(num))
main()'''
#009 tabuada
'''def main():
    valor=int(input('digite um valor para tabuada:'))
    print(f'{valor} x 1 = {valor} / {valor} x 2 = {valor*2}...')
main()'''
#011 pintando parede
'''def main():
    larg=float(input('qual a largura?'))
    alt=float(input('qual a altura?'))
    print (f'tem uma área de {larg*alt}m² e vai precisar de {(larg*alt)/2} litros')
main()'''   
#017 catetos e hipotenusa
def hipotenusa(catAd,catOp):
    return ((catAd**2+catOp**2)**(1/2))
'''print (f' a hipotesuca vai medir {hipotenusa(2,2.5):.2f}')'''
#018 seno, cos e tangente
import math
# se (from math import radians, sin, cos, tan) n precisa colocar todos os math
'''def main():
    ang=float(input('valor:'))
    seno = math.sin(math.radians(ang))
    print(f'o seno é {seno:.2f}')
    print(f'o cosseno é {math.cos(math.radians(ang)):.2f} e a tangente é {(math.tan(math.radians(ang))):.2f}')
main()'''
#019 sorteando um item na lista
def main():
