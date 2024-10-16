'''1- Crie a superclasse abstrata Carro
2- Crie o construtor com o atributo de instância modelo
3- Crie os métodos de instância get_modelo e set_modelo
4- Crie o método abstrato preço da diária
5- Crie um objeto da superclasse abstrata Carro, teste
6- Crie o atributo de classe preço base de locação com valor fixo de R$ 100.00
7a- Crie os métodos de classe get_preco_base e set_preco_base
7b- Altere o preço base de locação do carro, teste
8- Crie a subclasse Economico com o atributo modelo.
9- No construtor da subclasse, chame o construtor da superclasse e passe o modelo
10- Crie um objeto da subclasse Economico, teste
11- Sobrescreva o método abstrato da superclasse
    Obs.: RN (Regra de Negócio) para o carro econômico:
    O preço da diária corresponde ao preço base de locação acrescido de 5%
12- Crie um objeto da subclasse Economico, teste
13- Crie a subclasse Intermediário com o atributo modelo.
14- No construtor da subclasse, chame o construtor da superclasse e passe o modelo
15- Crie um objeto da subclasse Intermediário, teste
16- Sobrescreva o método abstrato da superclasse
    Obs.: RN (Regra de Negócio) para o carro intermediário:
    O preço da diária corresponde ao preço base de locação acrescido de 10%
17- Crie um objeto da subclasse Intermediário, teste

18- O sistema precisa informar a quantidade de objetos instanciados (cadastrados).
    Crie o atributo de classe para contar a quantidade de objetos instanciados (criados).
19- Atualize o construtor para implementar esse requisito (funcionalidade).
20- Crie o método de classe para consultar a quantidade de objetos instanciados
    (cadastrados). Teste'''

from abc import ABC, abstractmethod
class Carro(ABC):
    ct = 0
    @classmethod
    def qnt_obj_instanciados(cls):
        return cls.ct
    preco_base_locacao = 100.00 #atributo de classe global
    @classmethod
    def get_preco_base_locacao(cls):
        return cls.preco_base_locacao
    @classmethod
    def set_preco_base_locacao(cls, novo_preco_base):
        cls.preco_base_locacao = novo_preco_base

    def __init__(self, modelo):
        Carro.ct += 1
        self.modelo = modelo
    def get_modelo(self):
        return self.modelo

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    @abstractmethod
    def preco_diaria(self):
        pass

class Economico(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)

    def preco_diaria(self):
        return Carro.preco_base_locacao + 5/100 * Carro.preco_base_locacao

class Intermediario(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)

    def preco_diaria(self):
        return Carro.get_preco_base_locacao() + 10/100 * Carro.get_preco_base_locacao()

if __name__ == '__main__':
    # c1 = Carro('Nissan GTR')  NÃO POSSO CRIAR OBJETO DE SUPERCLASSE ABSTRATA
    # print(c1.get_modelo())

    print(f'Preço base de locação: {Carro.get_preco_base_locacao()}')

    Carro.set_preco_base_locacao(150.00)
    print(f'Novo preço base de locação: {Carro.get_preco_base_locacao()}')

    e1 = Economico('Gol quadrado 88')
    print(f'Modelo Econômico: {e1.get_modelo()}')
    print(f'Preço diária modelo econômico: {e1.preco_diaria()}')

    i1 = Intermediario('HB 20 Sedan')
    print(f'Modelo Intermediário: {i1.get_modelo()}')
    print(f'Preço diária modelo Intermediário: {i1.preco_diaria()}')

    i2 = Intermediario('Ford Ka Sedan')
    print(f'Modelo Intermediário: {i2.get_modelo()}')
    print(f'Preço diária modelo Intermediário: {i2.preco_diaria()}')

    print(f'Quantidade de objetos cadastrados: {Carro.qnt_obj_instanciados()}')