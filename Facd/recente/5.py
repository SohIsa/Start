from listaa import Pilha
def main ():
    tula = Pilha()
    chica = Pilha()
    pingo = Pilha()

    tula.push('oi')
    tula.push('como')
    tula.push('vai')

    pingo.push('vai')
    pingo.push('como')
    pingo.push('oi')

    while tula.getPilha():
      chica.push(tula.pop())
    if pingo.getPilha() == chica.getPilha():
      print ('palíndromo')
    else:
      print ('nem de longe')   

#fiquei sem saber se era apenas sobre os index ou se ia alem disso com  acada coisa escrita dentro de cada index

main()
