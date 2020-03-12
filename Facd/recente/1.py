from listaa import Pilha
def main ():
    texto = Pilha()
    for i in range(3):
        a=input('coisas:')
        if a == ('@'):
            texto.esvaziar()
        elif a == ('#'):
            texto.backspace()
        else:
            texto.push(a)
        print(texto.getPilha())
main()
