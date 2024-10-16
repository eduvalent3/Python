import datetime

class Pessoa(object):
    def __init__(self, nome, peso, altura, ano_nascimento = 2000):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.ano_nascimento = ano_nascimento

    def get_menu(self):
        return (f'''
            ----- Menu ----- 
            nome: {self.nome}
            peso: {self.peso}
            altura: {self.altura}
            ano de nascimento: {self.ano_nascimento}
            ''')

    def get_nome(self):
        return self.nome

    def get_peso(self):
        return self.peso

    def get_altura(self):
        return self.altura

    def set_nome(self, novo_nome):
        # if type(novo_nome) == str:
        #     self.nome = novo_nome
        # else:
        #     print('error')


        # if type(novo_nome) == type('a'):
        #     self.nome = novo_nome
        # else:
        #     print('error')

        # novo_nome_em_formato_de_string = str(novo_nome) # retorna True ou False
        # if novo_nome_em_formato_de_string.isnumeric():
        #     self.nome = novo_nome_em_formato_de_string
        # else:
        #     print('error')

        if isinstance(novo_nome, str):
            self.nome = novo_nome
        else:
            print('error')

    def get_ano_nascimento(self):
        return self.ano_nascimento

    def set_ano_nascimento(self, novo_ano_nascimento):
        self.ano_nascimento = novo_ano_nascimento

    def IMC(self):
        self.IMC = self.peso / (self.altura ** 2)
        return self.IMC

    def calcula_idade(self):
        data = datetime.date.today()
        # data = datetime.datetime.now() (outro jeito - até milisegundo)
        diferenca_de_anos = data.year - self.ano_nascimento
        return diferenca_de_anos

    def retorna_mais_velho(self, pessoa):
        if self.ano_nascimento > pessoa.ano_nascimento:
            return f'{self.nome} é mais velho que {pessoa.nome}'
        else:
            return f'{pessoa.nome} é mais velho que {self.nome}'

if __name__ == '__main__':
    pessoa1 = Pessoa('Carlos', 71, 1.80, 2000)
    print('Objeto criado:', pessoa1)

    pessoa2 = Pessoa('Pedro', 80, 1.75, 1995)
    print('Objeto criado:', pessoa2)

    pessoa3 = Pessoa('Paula', 52, 1.63, 2001)
    print('Objeto criado:', pessoa3)
    print('Nome da pessoa:', pessoa3.get_nome())
    print('Peso da pessoa 3:', pessoa3.get_peso())
    print('Altura da pessoa3:', pessoa3.get_altura())
    print('Ano de nascimento da pessoa 3:', pessoa3.get_ano_nascimento())

    pessoa4 = Pessoa('Ana', 54, 1.55)
    print('Ano de nascimento default pessoa 4:', pessoa4.get_ano_nascimento())

    print('Nome da pessoa1:', pessoa1.get_nome())
    print('Ano de nascimento:', pessoa1.get_ano_nascimento())

    novo2_nome = str(input('Digite o novo nome: '))

    pessoa1.set_nome(novo2_nome)
    print(pessoa1.get_nome())

    novo2_ano_nascimento = int(input(('Digite o novo ano de nascimento da pessoa 1: ')))

    pessoa1.set_ano_nascimento(novo2_ano_nascimento)
    print('Novo ano de nascimento da pessoa 1:', pessoa1.get_ano_nascimento())

    print(pessoa3.get_menu())

    print(pessoa1.retorna_mais_velho(pessoa2))