"""
1- Crie a classe Titular com os atributos cpf, nome, sobrenome, teste
2- E os métodos gets e sets, teste
3- Crie o método funcional nome_completo, teste
4- Crie um objeto da classe Titular
5- Crie a classe Conta com os atributos numero, obj_titular, saldo, limite.
6- Crie os métodos gets e sets
7- Crie um objeto da classe Conta usando o objeto titular criado
8- Mostre o endereço do objeto titular criado
9- Mostre o endereço do objeto conta criado
10- Mostre o nome, sobrenome e cpf usando o objeto titular
11- Altere o nome do objeto titular, teste.
12- Mostre o nome, sobrenome e cpf usando o objeto conta.
13- Altere o nome do objeto titular usando o objeto conta, teste.
14- Crie o método extrato_1 para mostrar os seguintes dados:
    número da conta e saldo da conta
15- Crie o método extrato_2 para mostrar os seguintes dados:
    nome, sobrenome, cpf, número da conta e saldo da conta
16- Mostre todos os dados do atributo titular da classe Conta

17- Faça um depósito, teste.
18- Faça um saque, teste.
19- Refaça o método anterior com críticas.
20- Cadastre mais uma conta corrente. Teste
21- Faça uma transferência, teste.
"""

class Titular(object):
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_sobrenome(self):
        return self.sobrenome
    def set_sobrenome(self, novo_sobrenome):
        self.sobrenome = novo_sobrenome

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def nome_completo(self):
        print(f'Seu nome completo é: ',self.nome, self.sobrenome)

class Conta(object):
    def __init__(self, numero, obj_titular, saldo, limite):
        self.numero = numero
        self.obj_titular = obj_titular
        self.saldo = saldo
        self.limite = limite

    def get_numero(self):
        return self.numero
    def set_numero(self, novo_numero):
        self.numero = novo_numero

    def get_obj_titular(self):
        return self.obj_titular
    def set_obj_titular(self, novo_obj_titular):
        self.obj_titular = novo_obj_titular

    def get_saldo(self):
        return self.saldo
    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def get_limite(self):
        return self.limite
    def set_limite(self, novo_limite):
        self.limite = novo_limite

    def extrato(self):
        return f'''
            Extrato:
    
            Nome do Titular: {self.obj_titular.get_nome()}
            Sobrenome do Titular: {self.obj_titular.get_sobrenome()}
            CPF do Titular: {self.obj_titular.get_cpf()}
            Numero da Conta: {self.numero}
            Saldo da Conta: {self.saldo}
            Limite da conta: {self.limite}'''

    def dados_titular(self):
        return f'''
        Nome: {self.obj_titular.get_nome()}
        Sobrenome: {self.obj_titular.get_sobrenome()}
        CPF: {self.obj_titular.get_cpf()}'''

    def deposito(self, valor):
        self.conta += valor

    def saque(self, valor):
        if valor <= self.conta:
            self.conta -= valor
        else:
            print('Você não possui saldo suficiente!')

    def transfere(self, destino):
        valor = float(input('Digite o valor que deseja transferir: '))
        if valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
        else:
            print('Você não possui saldo suficiente!')

if __name__ == '__main__':
    t1 = Titular('Eduardo', 'Barreto', 11111111111)
    print('Seu nome completo é: ',t1.get_nome(), t1.get_sobrenome())

    t1.nome_completo()

    c1 = Conta(123456, t1, 330.00, 10000)
    print(t1) #mostre o endereço do objeto titular criado
    print(c1) #mostre o endereço do objeto conta criado

    print(c1.extrato())

    print(c1.dados_titular())

    print(f'\nNome do titular: ',c1.get_obj_titular().get_nome())
    print(f'Sobrenome do titular: ',c1.get_obj_titular().get_sobrenome())
    print(f'CPF: ',c1.get_obj_titular().get_cpf())

    t2 = Titular('Daniel', 'Brito', 22222222222)
    print(f'Seu nome completo é: {t2.get_nome()} {t2.get_sobrenome()}')

    c2 = Conta(654321, t2, 1200.00, 5000)
    print(c2.dados_titular())

    c2.transfere(c1)

    print('Novo saldo de c1 é: ',c1.get_saldo())
    print('Novo saldo de c2 é: ',c2.get_saldo())