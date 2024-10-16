'''1- Crie a superclasse abstrata FormaGeometrica que herda de ABC (Abstract Base Classes)
2- Crie os dois métodos abstratos area e perímetro
3- Crie um objeto da superclasse abstrata FormaGeometrica, teste
4- Crie a subclasse Quadrado que herda da superclasse abatrata FormaGeometrica
5- Crie o construtor com o atributo lado, teste
6- Crie os métodos get e set, teste
7- Sobreescreva o método abstrato area da superclasse abstrata FormaGeometrica
   area = lado ao quadrado.
8- Crie um objeto da subclasse Quadrado, teste
9- Sobreescreva também o método perímetro da superclasse abstrata
   perimetro = 4 . lado
10- Crie um objeto da subclasse Quadrado, teste
11- Altere o valor do lado, teste
12- Crie a subclasse Circulo que herda da superclasse abstrata FormaGeometrica
13- Crie o construtor com o atributo raio, teste
14- Crie os métodos get e set, teste
15- Sobreescreva o método abstrato area da superclasse abstrata FormaGeometrica
    area = π . raio ao quadrado
16- Crie um objeto da subclasse Circulo, teste
17- Sobreescreva também o método perímetro da superclasse abstrata
    perimetro = 4 . π . raio
18- Crie um objeto da subclasse Circulo, teste
19- Refaça a subclasse Circulo com a constante pi do Python, mostre com duas casas decimais
20- Crie um método concreto na superclasse para mostrar uma menscagem fixa, teste

21- Crie mais um método concreto para mostrar uma mensagem na superclasse
    e identifique o objeto da subclasse que chamou o método, teste
22- Refaça o anterrior sem mostrar o endereço hexadecimal, mostre só o nome da classe

23- O sistema precisa informar quantas figuras geométricas foram cadastradas na
    memória (instanciadas). Para isso, crie o atributo de classe e o método de
    classe necessários para atender essa necessidade (funcionalidade).
    Esse método de classe não recebe nada e retorna a quantidade de figuras criadas.'''

from abc import ABC, abstractmethod
import math
class FormaGeometrica(ABC):
    ct = 0
    @classmethod
    def qnt_obj_cadastrados(cls):
        return cls.ct
    def __init__(self):
        FormaGeometrica.ct += 1
    @abstractmethod
    def area(self):
        ...
    @abstractmethod
    def perimetro(self):
        pass

    # @staticmethod
    def mensagem(self):
        return 'Teste de mensagem fixa'
    def mensagem2(self):
        print( 'Teste de mensagem fixa 2')
        print(self)
    def mensagem3(self):
        print( 'Teste de mensagem fixa 2')
        print(self.__class__)
    def mensagem4(self):
        print( 'Teste de mensagem fixa 2')
        print(self.__class__.__name__)


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
    def get_lado(self):
        return self.lado
    def set_lado(self, novo_lado):
        self.lado = novo_lado
    def area(self):
        return self.lado ** 2
    def perimetro(self):
        return self.lado * 4

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
        super().__init__()

    def get_raio(self):
        return self.raio


    def set_raio(self, novo_raio):
        self.raio = novo_raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

if __name__ == '__main__':
    q1 = Quadrado(5)
    print('A área do quadrado 1 é:', q1.area())
    print('O perímetro do quadrado 1 é:', q1.perimetro())
    print('O lado do quadrado 1 é:', q1.get_lado())
    q1.set_lado(8)
    print(f'O novo lado do quadrado 1 é: {q1.get_lado()}')

    c1 = Circulo(3)
    print('O raio do circulo 1 é: {:.2f}' .format(c1.get_raio()))
    print(f'A área do circulo 1 é: {c1.area():.2f}')
    print('O perímetro do circulo 1 é:', c1.perimetro())

    print('Quantidade de objetos cadastrados:', FormaGeometrica.qnt_obj_cadastrados())

    print(q1.mensagem())

    q1.mensagem2()

    c1.mensagem3()

    q1.mensagem4()