class Veiculo(object):
    def __init__(self, valor, modelo, km = 1):
        self.valor = valor
        self.modelo = modelo
        self.km = km

    def get_valor(self):
        return self.valor

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_km(self):
        return self.km

    def set_km(self, novo_km):
        self.km = novo_km

    def atualiza_valor(self, acrescenta_valor):
        if type(acrescenta_valor) == float:
            self.valor = self.valor + acrescenta_valor
        else:
            print('Você digitou um valor inválido!!!')

    def atualiza_valor_pct(self, valor_porcentagem):
        if type(valor_porcentagem) == int:
            self.valor = self.valor * (valor_porcentagem / 100) + self.valor
        else:
            print('Você digitou um valor inválido!!!')

class Carro(Veiculo):
    def __init__(self, valor, modelo, km = 1, qtd_portas = 4):
        super().__init__(valor, modelo, km)
        self.qtd_portas = qtd_portas

    def __str__(self):
        return (f'''
        Valor: {self.valor}
        Modelo: {self.modelo}
        Quilometragem: {self.km}
        Quantidade de Portas: {self.qtd_portas} ''')

class Moto(Veiculo):
    def __init__(self, valor, modelo, km = 1, cilindradas = 125):
        super().__init__(valor, modelo, km)
        self.cilindradas = cilindradas

    def get_cilindradas(self):
        return self.cilindradas

    def set_cilindradas(self, nova_cilindrada):
        self.cilindradas = nova_cilindrada

if __name__ == '__main__':
    c1 = Carro(60000.00, 'Ford Ka', 0.00, 4)
    print(f'Carro 1: {c1}')

    c2 = Carro(150000.00, 'Corolla', 15000.00)
    print(f'Carro 2: {c2}')

    c3 = Carro(300000.00, 'Camaro')
    print('Carro 3', c3)

    m1 = Moto(40000.00, 'Ninja', 0.00, 1000)
    print('Moto 1:', m1)

    m2 = Moto(25000.00, 'Yamaha', 10000.00)
    print('Moto 2:', m2)

    print(f'Usando método vars: {vars(c1)}')

    print(f'Usando método Dict: {c2.__dict__}')

    c1.atualiza_valor(5000.00)
    print('Atualizando o valor do carro 1 em 5 mil:', c1.get_valor())

    m1.atualiza_valor_pct(20)
    print('Aumentando o valor da Moto 1 em 20%:', m1.get_valor())