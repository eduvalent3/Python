class Estacionamento(object):
    def __init__(self, placa_do_carro = 'default', modelo_do_carro = 'default', horario_de_entrada = 00.00, horario_de_saida = 00.00):
        self.placa_do_carro = placa_do_carro
        self.modelo_do_carro = modelo_do_carro
        self.horario_de_entrada = horario_de_entrada
        self.horario_de_saida = horario_de_saida

    def get_placa_do_carro(self):
        return self.placa_do_carro
    
    def set_placa_do_carro(self, nova_placa_do_carro):
        self.placa_do_carro = nova_placa_do_carro

    def get_modelo_do_carro(self):
        return self.modelo_do_carro
    
    def set_modelo_do_carro(self, novo_modelo_do_carro):
        if type(novo_modelo_do_carro) == str:
            self.modelo_do_carro = novo_modelo_do_carro
        else:
            return('Você não digitou um modelo de carro válido')

    def get_horario_de_entrada(self):
        return self.horario_de_entrada
    
    def set_horario_de_entrada(self, novo_horario_de_entrada):
        self.horario_de_entrada = novo_horario_de_entrada

    def get_horario_de_saida(self):
        return self.horario_de_entrada
    
    def set_horario_de_saida(self, novo_horario_de_saida):
        self.horario_de_saida = novo_horario_de_saida

    def valor_a_pagar(self):
        if self.horario_de_saida - self.horario_de_entrada > 0.15:
            return (self.horario_de_saida - self.horario_de_entrada) * 5
        else:
            return ('Você não excedeu o tempo de 15min')
        
    def desconto(self):
        if self.horario_de_saida - self.horario_de_entrada <= 3.00:
            return (self.horario_de_saida - self.horario_de_entrada) * 3.5
        else:
            return ('Você não possui desconto')

    def __str__(self):
        return(f'''
        Placa do Carro: {self.placa_do_carro}
        Modelo do Carro: {self.modelo_do_carro}
        Horário de Entrada: {self.horario_de_entrada}
        Horário de Saída: {self.horario_de_saida}
''')

if __name__ == '__main__':
    carro1 = Estacionamento('JJJ-1111', 'Ford Ka', 18.56, 22.13)
    print('Carro 1 criado:', carro1.__str__())

    print(f'O Valor a pagar do carro {carro1.get_modelo_do_carro()} é {carro1.valor_a_pagar()} reais')

    print(carro1.desconto())

    carro1.set_placa_do_carro('TTT-5555')
    print(f'A nova placa do {carro1.get_modelo_do_carro()} é {carro1.get_placa_do_carro()}')

    carro1.set_modelo_do_carro('Ford Maverick')
    print(f'O novo modelo do carro 1 é {carro1.get_modelo_do_carro()}')

    carro1.set_horario_de_entrada(13.45)
    print(f'A nova hora de entrada do carro 1 é {carro1.get_horario_de_entrada()}')

    carro1.set_horario_de_saida(19.34)
    print(f'A nova hora de saída do carro 1 é {carro1.get_horario_de_saida()}')

    carro2 = Estacionamento('HHH-2222', 'Nissan GTR', 13.44)
    print('Carro 2 criado:', carro2.__str__())

    carro3 = Estacionamento('FFF-3333', 'Chevrolet Prisma')
    print('carro 3 criado:', carro3.__str__())

    carro4 = Estacionamento('GGG-4444')
    print('carro 4 criado:', carro4.__str__())
