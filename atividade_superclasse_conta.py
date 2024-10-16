class Conta(object):
    def __init__(self, nome, saldo = 0.0):
        self.nome = nome
        self.saldo = saldo

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def __str__(self):
        return (f'''
        Nome: {self.nome}
        Saldo: {self.saldo}''')

    def deposito(self, valor_deposito):
        self.saldo = self.saldo + valor_deposito

    def retirada(self, retirada):
        if retirada <= self.saldo:
            self.saldo = self.saldo - retirada
            return ('Seu novo saldo é:', self.saldo)
        else:
            return('Saldo Insuficiente, seu saldo é de:', self.saldo)

class Conta_pessoa_fisica(Conta):
    def __init__(self, nome, saldo, genero, cpf):
        super().__init__(nome, saldo)
        self.genero = genero
        self.cpf = cpf

    def get_genero(self):
        return self.genero

    def set_genero(self, novo_genero):
        self.genero = novo_genero

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def __str__(self):
        return (f'''{super().__str__()}
        Genero: {self.genero}
        CPF: {self.cpf}''')

class Conta_pessoa_juridica(Conta):
    def __init__(self, nome, saldo, modalidade, cnpj):
        super().__init__(nome, saldo)
        self.modalidade = modalidade
        self.cnpj = cnpj

    def get_modalidade(self):
        return self.modalidade

    def set_modalidade(self, nova_modalidade):
        self.modalidade = nova_modalidade

    def get_cnpj(self):
        return self.cnpj

    def set_cnpj(self, novo_cnpj):
        self.cnpj = novo_cnpj

    def __str__(self):
        return (f'''{super().__str__()}
        Modalidade: {self.modalidade}
        CNPJ: {self.cnpj}''')

if __name__ == '__main__':
    c1 = Conta('Alice')
    print(c1)

    conta_pf1 = Conta_pessoa_fisica('Cleuson', 15000.00, 'Masculino', '111.111.111-11')
    print(conta_pf1)

    conta_pj1 = Conta_pessoa_juridica('Xbox Mil Grau', 0.0, 'Microempreendedor', '222.222.222')
    print(conta_pj1)

    print(vars(conta_pf1))

    print(conta_pj1.__dict__)
