class Funcionario(object):
    def __init__(self, cpf, nome, salario = 0.0):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_salario(self):
        return self.salario

    def set_salario(self, novo_salario):
        self.salario = novo_salario

    def __str__(self):
        return (f'''
        CPF: {self.cpf}
        Funcionário:{self.nome}
        Salário:{self.salario}
''')

    def bonificacao_todos_funcionarios(self):
        bonificacao = self.salario * 10 / 100
        return bonificacao

class Gerente(Funcionario):
    def __init__(self, cpf, nome, salario, senha, qtd_funcionarios_gerenciados):
        #self.cpf = cpf
        #self.nome = nome
        #self.salario = salario
        super().__init__(cpf, nome, salario)
        self.senha = senha
        self.qtd_funcionarios_gerenciados = qtd_funcionarios_gerenciados

    def __str__(self):
        s1 = super().__str__()
        s = (f'''{s1}
        Quantidade de Funcionarios Gerenciados: {self.qtd_funcionarios_gerenciados}"
        Senha: {self.senha}''')
        return s

    def autentica(self):
        senha = input(f'Senha de acesso do Gerente {self.nome}: ')
        if senha == self.senha:
            return('Acesso permitido')
        else:
            return('Acesso negado!!!')

if __name__ == '__main__':
    f1 = Funcionario('123.456.789.10', 'Paulo', 1000.00)
    print(f'Funcionário 1 criado: {f1}')

    f2 = Funcionario('000.000.000.00', 'Lucas')
    print(f'Funcionário 2 criado: {f2}')

    g1 = Gerente('111.111.111.11', 'Leôncio', 9000.00, '12345', 20)
    print(f'Gerente 1 criado: {g1}')

    print(g1.autentica())

    g2 = Gerente('222.222.222.22', 'João', 12000.00, '54321', 5)
    print(f'Gerente 2 criado: {g2}')

    print(g2.autentica())

    #print(f1.autentica())

    print(f'A Bonificação do funcionário Paulo é: {f1.bonificacao_todos_funcionarios()}')

    print(f'A Bonificação do Gerente Leôncio é: {g1.bonificacao_todos_funcionarios()}')

    print(f'Outro método parecido com str: {vars(g1)}')

    print(f'Outro método parecido com str: {g1.__dict__}')

class Vendedor(Funcionario):
    def __init__(self, cpf, nome, salario, valor_vendas, porcentagem_vendas):
        super().__init__(cpf, nome, salario)
        self.valor_vendas = valor_vendas
        self.porcentagem_vendas = porcentagem_vendas

    def __str__(self):
        s1 = super().__str__()
        s = (f'''{s1}
        Valor Vendas: {self.valor_vendas}"
        Porcentagem das Vendas: {self.porcentagem_vendas}''')
        return s

if __name__ == '__main__':
    v1 = Vendedor('999.999.999.99', 'Jailson Mendes', 1500.00, 50000.00, 0.08)
    print(f'Vendedor criado: {v1}')