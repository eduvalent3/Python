'''
1- Crie um novo projeto e a classe Point.
2- Crie o método construtor, ele atribui o valor default zero para os parâmetros
   de x e y
3- No construtor, crie os atributos x e y.
4- Na função main, crie o objeto p1 (ponto p1) sem passar argumentos. Teste
5- Crie os métodos gets e sets.
6- Mostre o valor do atributo x e y.
7- Faça pelo menos uma crítica no método set_x (evitar dados inconsistentes), teste
8- Na função main, crie o objeto p2 (ponto p2) passsndo os valores 2 e 3 como argumento.
   Teste
9- Sobrescreva o método __str__. Ele recebe self e retorna todos os atributos concatenados.
   Teste
10- Na função main, crie o objeto p3 (ponto p3) passsndo somente o argumento x. Teste
11- Na função main, crie o objeto p4 (ponto p4) passsndo somente o argumento y. Teste
12- Crie o método distância de um ponto qualquer a origem (0, 0) do plano cartesiano.
    Ele retorna o valor calculado.
    distancia = raiz_quadrada((x1-x2)^2 + (y1-y2)^2) - Obs.: (x1-x2)^2 elevado ao quadrado
    Teste 1: (p2) x = 2 e y = 3                 Distância = 3.605551275463989
    Teste 2: (p4) x = 0 e y = 5                 Distância = 5
13- Crie método distancia_dois_pontos, ele retorna a distância de dois pontos quaisquer
    no plano
    Teste 1: P2 (2, 3) e P3 (3, 0)              Distância:  3.1622776601683795
    Teste 2: P2 (2, 3) e P4 (0, 5)              Distância:  2.8284271247461903
14- Crie o método mostra_mais_distante_origem, ele compara dois pontos quaisquer e mostra o
    ponto mais distante da origem

15- Crie o método retorna_mais_distante_origem, ele compara dois pontos quaisquer e retorna
    o ponto (objeto) mais distante da origem. Teste
16- Crie o método mostra_ponto_medio, ele calcula e mostra o ponto médio entre dois pontos
    quaisquer. Teste.
17- Crie o método retorna_obj_ponto_medio, ele calcula o ponto médio entre dois pontos quaisquer,
    cria um novo objeto e retorna esse objeto pro main. Teste.
'''

from math import sqrt
class Point(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, valor):
        self.x = valor

    def get_y(self):
        return self.y

    def set_y(self, valor):
        self.y = valor

    def __str__(self):
        return (f'''
        Coordenada X: {self.x}
        Coordenada Y: {self.y}
    ''')

    def distancia_ponto_origem(self):
       return sqrt((self.x)**2 + (self.y)**2)

    def distancia_dois_pontos(self, ponto):
        return sqrt((self.x - ponto.get_x())**2) + ((self.y - ponto.get_y())**2)

    def mostra_mais_distante_origem(self, ponto2):
        if self.distancia_ponto_origem() > ponto2.distancia_ponto_origem():
            print(f'O ponto {self.x, self.y} está mais distante que o ponto {ponto2.get_x(), ponto2.get_y()} ')
        else:
            print(f'O ponto {ponto2.get_x(), ponto2.get_y()} está mais distante que o ponto {self.x, self.y} ')

    def mostra_mais_distante_origem(self, ponto2):
        if self.distancia_ponto_origem() > ponto2.distancia_ponto_origem():
            return(f'O ponto {self.x, self.y} está mais distante que o ponto {ponto2.get_x(), ponto2.get_y()} ')
        else:
            return(f'O ponto {ponto2.get_x(), ponto2.get_y()} está mais distante que o ponto {self.x, self.y} ')

    def mostra_ponto_medio(self, objeto2):
        print(f'O ponto médio entre o ponto {self.x, self.y} e o ponto {objeto2.get_x(), objeto2.get_y()} é: '
              f'{(self.x + objeto2.get_x())/2, (self.y + objeto2.get_y())/2}')

    def retorna_objeto_ponto_medio(self, objeto2):
        x= (self.x + objeto2.get_x())/2
        y= (self.y + objeto2.get_y())/2
        o_med = Point(x, y)
        return o_med

if __name__ == '__main__':
    ponto1 = Point()
    print('Objeto ponto1 da classe point:', ponto1)

    ponto2 = Point(2, 3)
    print('Objeto ponto2 da classe point:', ponto2)

    ponto3 = Point(1)
    print('Objeto ponto3 da classe point:', ponto3)

    ponto4 = Point(y = 2)
    print('Objeto ponto4 da classe point:', ponto4)

    print(f'A distancia do ponto 2 a origem é: {ponto2.distancia_ponto_origem()}')

    print(f'A distancia do ponto 2 para o ponto 3 é: {ponto2.distancia_dois_pontos(ponto3)}')

    ponto2.mostra_mais_distante_origem(ponto3)

    print(ponto2.mostra_mais_distante_origem(ponto3))

    ponto2.mostra_ponto_medio(ponto3)

    ponto2.mostra_ponto_medio(ponto3)

    ponto_medio = ponto1.retorna_objeto_ponto_medio(ponto2)
    print(ponto_medio.__str__())
