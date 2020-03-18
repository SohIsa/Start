from pili import Pilha
def main ():
    s1 = Pilha()
    s1ad = Pilha()
    variavelad = []
    for i in range(3):
      s1.push(i)
    print (s1.getPilha())
    while s1.getPilha():
      s1ad.push(s1.pop())
    print(s1ad.getPilha())
    while s1ad.getPilha():
      s1.push(s1ad.pop())
    print(s1.getPilha())

    #variável que não pilha
    s12 = Pilha()
    s12.push('um')
    s12.push('dois')

    for i in s12.getPilha():
      variavelad.append(i)
    print (variavelad)

main()
