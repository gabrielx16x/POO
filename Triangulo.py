from Ponto import Ponto

P1 = Ponto(2,6)
P2 = Ponto(2,4)
P3 = Ponto(13,22)
class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calc_lado(self, A, B):
        return Ponto.calc_dist_entre_pontos(A,B)
    
    def calc_area(self):
        la = self.calc_lado(self.b, self.c)
        lb = self.calc_lado(self.a, self.c)
        lc = self.calc_lado(self.a, self.b)
        s = (la + lb + lc) / 2
        area = (s * (s - la) * (s - lb) * (s - lc)) ** 0.5
        return area
    
    def verifica(self):
        la = self.calc_lado(self.b, self.c)
        lb = self.calc_lado(self.a, self.c)
        lc = self.calc_lado(self.a, self.b)
        if la != lb and lb != lc and la != lc:
            return "Escaleno"
        elif la == lb == lc:
            return "Equilátero"
        else:
            return "Isósceles"
Tri = Triangulo(P1,P2,P3)

print(Tri.calc_lado(P1,P3))
print(Tri.calc_area())

print(Tri.verifica())
