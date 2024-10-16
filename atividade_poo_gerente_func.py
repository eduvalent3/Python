'''
1- Crie a classe Funcionario e o construtor, def __init___ (self, ...),
   da classe com os atributos cpf, nome e salario
2- Crie uma instância (objeto) da classe com os dados necessários
   (f1 = Funcionario()), teste
3- Crie alguns métodos get e set. Teste
4- Crie um segundo funcionário passando apenas o cpf e o nome. Teste
5- Sobrescreva o método __str__. Ele retorna os dados do funcionário
   concatenados. Teste.
6a- Crie a classe Gerente e o construtor com os atributos cpf, nome, salario,
    senha e a quantidade de funcionários que ele gerencia.
6b-Crie uma instância (objeto) da classe Gerente com os dados necessários, teste
7- Crie alguns métodos gets e sets. Teste
8- Mostre todos os dados (atributos) do objeto g1 da classe Gerente, conseguiu
   usando o __str__?
9- Crie o método autentica na classe Gerente. Ele recebe o objeto, o usuário
   digita a senha e verifica se a senha digitada é igual a senha armazenada
   na memória (self.senha). imprime: "Acesso permitido." ou "Acesso negado."
   e retorna o valor booleano True ou False.
10- Use o método autentica para o gerente instanciado (objeto g1).
11- Use o método autentica para o funcionario instanciado (objeto f1).
    Por quê deu erro?
12- Crie outra instância (objeto g2) da classe Gerente com os dados necessários.
13- Use o método __str__ para o gerente (objeto g2). Por quê mostrou endereço
    hexadecimal?
14- Use todos os métodos da classe Gerente para o gerente g2.
'''

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

class Gerente(object):
    def __init__(self, cpf, nome, salario, senha, qtd_funcionarios_gerencia):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario
        self.senha = senha
        self.qtd_funcionarios_gerencia = qtd_funcionarios_gerencia

    def __str__(self):
        return(f'''
        CPF: {self.cpf}
        Gerente:{self.nome}
        Salário: {self.salario}
        Senha: {self.senha}
        Quantida de Funcionários que gerencia: {self.qtd_funcionarios_gerencia}      
''')

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