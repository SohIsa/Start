class Retangulo:
    #construtor
    def __init__(self,base,altura):
        #atributos
        self.ba = base
        self.alt = altura
     #outros métodos
    def area (self):
        return (self.ba*self.alt)
r1 = Retangulo(10, 2)
print(r1.area())
