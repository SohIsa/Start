#1
'''def main ():
    idade=int(input('em que ano você nasceu?'))
    print (f'você tem {(2020-idade)*365} dias')
main ()  '''
#2
'''def area (bas,alt):
    return bas*alt/2
def main():
    base,altura=input('base e altura?').split()
    base,altura=float(base), float(altura)  
    print (area(base,altura))
main()'''
#3
'''valor=float(input('diga um valor:'))
if valor>10:
    print ('É MAIOR QUE 10!')
else:
    print('NÃO É MAIOR QUE 10!')'''
#5
'''def preço(qtde):
    if qtde<12:
        return (qtde*1.30)
    else:
        return (qtde)
def main():
    maça=int(input('quantas maçãs?'))
    print (preço(maça))
main()'''
#4
'''valor=float(input('número:'))
if valor>=0:
    print ('positivo')
else:
    print ('negativo')'''
#6
'''def media(nota1,nota2,nota3):
    if nota1>nota2 and nota1>nota3:
        return ((nota1*4)+(nota2*3)+(nota3*3))/10
    elif nota2>nota1 and nota2>nota3:
        return ((nota2*4)+(nota1*3)+(nota3*3))/10
    else:
        return ((nota3*4)+(nota1*3)+(nota2*3))/10
def main ():
    cod=int(input('qual o seu código:'))
    pont1=int(input('nota:'))
    pont2=int(input('nota:'))
    pont3=int(input('nota:'))
    if (media(pont1,pont2,pont3))>=5:
        print(f'Código {cod} você foi APROVADO com média {(media(pont1,pont2,pont3))} tendo notas {pont1}, {pont2} e {pont3}')
    else:
        print(f'Código {cod} você foi REPROVADO com média {(media(pont1,pont2,pont3))} tendo notas {pont1}, {pont2} e {pont3}')
main()'''
#7
'''def main():
    valor1=int(input('número:'))
    valor2=int(input('número:'))'''
#8 - 10
'''def main():
    valor1=int(input('primeira nota:'))
    valor2=int(input('segunda nota:'))
    while valor1<0 or valor1>10:
        print ('primeira nota invalida')
        valor1=int(input('primeira nota:'))
    while valor2<0 or valor2>10:
        valor1=int(input('segunda nota:'))
    print ((valor1+valor2)/2)
main ()'''
#11
'''def main ():
    nota1=int(input('nota:'))
    nota2=int(input('nota:'))
    while nota2<0 and nota2>10:
        print('nota invalida')
        nota1=int(input('nota:'))
        nota2=int(input('nota:'))
        print ((nota1+nota2)/2)
main()'''
#12
'''cres=[]
for i in range(10):
    cres.append(input(f'números:'))
print(sorted(cres))'''
#13
'''for i in range(10,-1,-1):
    print (i)'''
#14
'''def main ():
    soma=0
    for i in range(10):
        num=int(input('números:'))
        soma+=num
    print(soma)    
main()'''
#15
'''def main ():
    soma=0
    totalmecadoria=int(input('quantas mercadorias?'))
    for i in range (totalmecadoria):
        valormercadoria=int(input('quanto custou?'))
        soma+=valormercadoria
    print(f'o valor total em estoque foi de {soma}')
    print(f'a média dos valores das mercadorias {soma/totalmecadoria}')
main()'''
