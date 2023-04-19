#Alunos: Maria Eduarda Tavares Mendes e Ant. Gabriel de Oliveira Valentin

#1. Crie uma classe chamada Ponto e salve em um mesmo arquivo .py esta classe e o arquivo
#principal indicando o uso de cada uma das questões. Essa classe deve receber dois valores X,
#Y (float) no seu construtor. Faça os getters e setters para esses atributos.
class Ponto:
    #Criação da classe Ponto
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property #Getter do x
    def x(self):
        return self._x

    @x.setter #Setter do x
    def x(self, novo_x):
        if self._x >= 0:
        
            self._x = novo_x
        elif self._x < 0:
           
            self._x = novo_x
    @property #Getter do y
    def y(self):
        return self._y

    @y.setter #Setter do y
    def y(self, novo_y):#3. Adicione uma proteção ao setter da classe para permitir apenas coordenadas nos quadrantes 1 e 2 (incluindo os eixos).
        if self._y >= 0:
            self._y = novo_y
        else: 
            print("Valor não permitido!")
    
#2. Adicione um método de instância à classe Ponto chamado get_info(). Esse método deve
#retornar as coordenadas e o quadrante daquele ponto.
    def get_info(self):
        quadrante = ''
        if self.x > 0 and self.y > 0:
            quadrante = 'Quadrante 1'
        elif self.x < 0 and self.y > 0:
            quadrante = 'Quadrante 2'
        elif self.x < 0 and self.y < 0:
            quadrante = 'Quadrante 3'
        elif self.x > 0 and self.y < 0:
            quadrante = 'Quadrante 4'
        return self.x, self.y, quadrante
    
#4. Crie um método de classe chamado por_tamanho_e_quadrante(t, q) para que o usuário
#consiga criar uma ponto com um determinado tamanho em um determinado quadrante.
    @classmethod
    def por_tamanho_e_quadrante(cls, t, q):
        hipotenusa = t
        cateto = hipotenusa * 0.75
        x = cateto
        y = cateto
        if q == 2:
            x = -cateto
        elif q == 3:
            x = -cateto
            y = -cateto
        elif q == 4:
            y = -cateto
        return cls(x, y)
    
#5. Adicione um método estático à classe Ponto chamado calc_dist_entre_pontos(p1, p2) que
#retornará a distância entre duas instâncias da classe Ponto.
    @staticmethod
    def calc_dist_entre_pontos(p1, p2):
        cateto1 = p2.y - p1.y
        cateto2 = p2.x - p1.x
        hipotenusa =(cateto1**2 + cateto2**2)**0.5 #Não usamos o math por que na calculadora deu o mesmo resultado.
        return hipotenusa



P = Ponto(2,3)
