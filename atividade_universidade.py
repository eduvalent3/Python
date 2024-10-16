'''1- Crie um projeto usando os conceitos de POO com herança (inheritance) contendo a
   superclasse (classe pai) Pessoa e duas subclasses (classes filhas) Professor e
   Funcionário.
2- Crie a superclasse Pessoa e o construtor com os atributos de instância nome
   e dependente, use valores defaults.
3- Crie os métodos get e set referente ao atributo nome e dependente. Faça crítica no
   set dependente.
4- Crie um objeto da classe Pessoa, cadastre uma pessoa para testar a classe Pessoa
5- A subclasse Professor tem os atributos de instância nome, dependente, qtd_turma
   e valor em reais por turma.
6- O construtor da subclasse Professor recebe os três parâmetros e chama o construtor
  da superclasse enviado o nome e a quantidade de dependente. E armazena o valor
  dos atributos qtd_turma e valor em reais por turma.
7- Use valores defaults (padrões) no construtor. Teste
8a- Cadastre um professor no sistema, ou seja, crie um objeto da subclasse Professor
8b- Use alguns métodos get e set dos atributos
9- Cadastre o segundo professor passando somente o nome e a qtd de dependentes
10- Cadastre o terceiro professor sem passar nenhum dado
11- Cadastre o quarto professor passando somente o nome e a qtd de turmas
12- Use alguns métodos get e set dos atributos
13- No método set referente ao atributo qtd_turma, faça pelo menos uma crítica.
14- Crie o método rendimentos, ele não recebe nada, calcula os rendimentos do
    professor e mostra o valor dos rendimentos do professor. O objetivo
    é calcular e mostrar os rendimentos do professor que depende da
    quantidade de turmas e do valor que ele ganha por turma.
15- A subclasse Funcionário tem os atributos de instância nome, dependentes
    e salario fixo
- Crie o construtor (__init__) da subclasse com valores defaulf
17- Cadastre o funcionário 1 no sistema passando os três atributos
- Cadastre o funcionário 2 no sistema passando apenas dois atributo
- Cadastre o funcionário 3 no sistema sem passar os atributos
20- Use alguns métodos get e set dos atributos
- No método set referente ao atributo salario, faça pelo menos uma crítica.
22- Para cada dependente, a empresa vai dá um valor extra de cem reais.
- Crie o método salário total considerando o valor extra.
24- Crie o método mostra dados pra mostrar os atributos do professor e do funcionário
25- Elabore e implemente o enunciado de mais um método funcional que você acha
    importante para o sistema.
26- O sistema precisa informar quantas pessoas tem cadastradas (instanciadas).
27- Crie o atributo de classe e o método de classe necessários para atender essa
    necessidade.'''

class Pessoa(object):
    ct = 0  #contador global
    @classmethod
    def quantidade_pessoas_cadastradas(cls):
        return cls.ct
    def __init__(self, nome = 'default', dependente = 0):
        self.nome = nome
        self.dependente = dependente
        Pessoa.ct += 1
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_dependente(self):
        return self.dependente
    def set_dependente(self, novo_dependente):
        self.dependente = novo_dependente

class Professor(Pessoa):
    def __init__(self, nome = 'default', dependente = 0, qtd_turma = 1, valor_por_turma = 1):
        super().__init__(nome, dependente)
        self.qtd_turma = qtd_turma
        self.valor_por_turma = valor_por_turma

    def get_qtd_turma(self):
        return self.qtd_turma

    def set_qtd_turma(self, nova_qtd_turma):
        if type(nova_qtd_turma) != str:

            if nova_qtd_turma >= 0:
                self.qtd_turma = nova_qtd_turma
                print(f'O novo número de turmas é: {self.qtd_turma}')
            else: print('O valor tem que ser maior que zero')

        else: print('Você não digitou um valor válido')

    def get_valor_por_turma(self):
        return self.valor_por_turma

    def rendimentos(self):
        print(self.qtd_turma * self.valor_por_turma)

    def mostra_dados(self):
        return (f'''
        Nome: {self.nome}
        Dependentes: {self.dependente}
        Quantidade de turmas: {self.qtd_turma}
        Valor ganho por turma: {self.valor_por_turma}''')

class Funcionario(Pessoa):
    def __init__(self, nome = 'default', dependente = 0, salario_fixo = 0.0):
        super().__init__(nome, dependente)
        self.salario_fixo = salario_fixo

    def get_salario_fixo(self):
        return self.salario_fixo

    def set_salario_fixo(self, novo_salario):
        self.salario_fixo = novo_salario

    def salario_total(self):
        print(self.salario_fixo + 100 * self.dependente)

    def mostra_dados(self):
        return (f'''
        Nome: {self.nome}
        Dependentes: {self.dependente}
        Salário fixo: {self.salario_fixo}''')

if __name__ == '__main__':
    print("ccccc", Pessoa.quantidade_pessoas_cadastradas())
    pessoa1 = Pessoa('Chief', 2)
    print(pessoa1.get_nome(), pessoa1.get_dependente())
    print("ccccc", Pessoa.quantidade_pessoas_cadastradas())

    pessoa1.set_nome('Nando Moura')
    print(f'O novo nome do professor 1 é: {pessoa1.get_nome()}')

    professor1 = Professor('Cleber', 3, 5, 600)
    print(professor1.get_nome(), professor1.get_dependente(), professor1.get_qtd_turma(), professor1.get_valor_por_turma())

    professor2 = Professor('Lucas', 2)
    print(professor2.get_nome(), professor2.get_dependente(), professor2.get_qtd_turma(), professor2.get_valor_por_turma())

    professor3 = Professor()
    print(professor3.get_nome(), professor3.get_dependente(), professor3.get_qtd_turma(), professor3.get_valor_por_turma())

    professor4 = Professor('Gustavo Fring', qtd_turma = 3)
    print(professor4.get_nome(), professor4.get_dependente(), professor4.get_qtd_turma(),professor4.get_valor_por_turma())

    professor1.set_qtd_turma(0)

    funcionario1 = Funcionario('Peter Turguniev', 5, 1500)
    print(funcionario1.get_nome(), funcionario1.get_dependente(), funcionario1.get_salario_fixo())

    funcionario2 = Funcionario('Kleyberton', 2)
    print(funcionario2.get_nome(), funcionario2.get_dependente(), funcionario2.get_salario_fixo())

    funcionario3 = Funcionario()
    print(funcionario3.get_nome(), funcionario3.get_dependente(), funcionario3.get_salario_fixo())

    print("ccccc", Pessoa.quantidade_pessoas_cadastradas())
