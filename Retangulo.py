from Ponto import Ponto

P1 = Ponto(-2, 0)
P2 = Ponto(-2, 5)
P3 = Ponto(4, 5)
P4 = Ponto(4, 0)
class Retangulo:
    def __init__(self, ponto1, ponto2, ponto3, ponto4):
        self.a = ponto1
        self.b = ponto2
        self.c = ponto3
        self.d = ponto4

    def calc_perimetro(self):
        l1 = Ponto.calc_dist_entre_pontos(self.a, self.b)#reutilização de código
        l2 = Ponto.calc_dist_entre_pontos(self.b, self.c)
        perimetro = 2 * (l1 + l2)#Cálculo que define o perímetro
        return perimetro

    def calc_area(self):
        l1 = Ponto.calc_dist_entre_pontos(self.a, self.b)#reutilização de código
        l2 = Ponto.calc_dist_entre_pontos(self.b, self.c)
        area = l1 * l2 #Cálculo que define a área
        return area

Ret = Retangulo(P1,P2,P3,P4)

print(Ret.calc_perimetro())
print(Ret.calc_area())
