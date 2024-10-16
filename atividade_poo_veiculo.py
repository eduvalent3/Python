class Veiculo(object):
    def __init__(self, modelo, ano, valor=0):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, novo_modelo):
        if isinstance(novo_modelo, str):
            self.modelo = novo_modelo
        else:
            print('Dado inconsistente')

    def get_ano(self):
        return self.ano

    def set_ano(self, novo_ano):
        if novo_ano > 0:
            self.ano = novo_ano
        else:
            print('Dado inconsistente')

    def get_valor(self):
        return self.valor

    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print('Error: valor inconsistente')

    def mostra_dados(self):
        print('- modelo:', self.modelo)
        print('ano:', self.ano)
        print('valor:', self.valor)

    def retorna_dados(self):
        return f'{self.get_modelo()}, {self.get_ano()}, {self.get_valor()}'

    def aumento_valor(self, aumento):
        self.valor += aumento


if __name__ == '__main__':
    carro1 = Veiculo('Opalão', 1971, 120000.00)
    print('Objeto carro 1:', carro1)
    carro2 = Veiculo('Maverick', 1976, 280000.00)
    print('Objeto carro 2:', carro2)

    print(carro1.get_modelo())
    print(carro1.get_ano())
    print(carro1.get_valor())
    print(carro2.get_modelo())
    print(carro2.get_ano())
    print(carro2.get_valor())

    carro1.set_modelo('Lamborghini Aventador')
    carro1.set_ano(2015)
    carro1.set_valor(1500000.00)
    carro2.set_modelo('Carro do 007')
    carro2.set_ano(1960)
    carro2.set_valor(9999999999.99)

    print(carro1.get_modelo())
    print(carro1.get_ano())
    print(carro1.get_valor())
    print(carro2.get_modelo())
    print(carro2.get_ano())
    print(carro2.get_valor())

    aumento_v = float(input('Digite o aumento do valor: '))
    carro1.aumento_valor(aumento_v)
    print(carro1.get_valor())

    carro3 = Veiculo('Ferrari', 2002)
    print(carro3.get_modelo())
    print(carro3.get_valor())
