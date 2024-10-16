class Videogame(object):
    def __init__(self, modelo, marca = 'Default', valor = 0):
        self.modelo = modelo
        self.marca = marca
        self.valor = valor

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        if type(novo_modelo) == str:
            self.modelo = novo_modelo
        else:
            print('Dado inconsistente')

    def get_marca(self):
        return self.marca
    def set_marca(self, nova_marca):
        if type(nova_marca) == str:
            self.marca = nova_marca
        else:
            print('Dado inconsistente')

    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print('Erro: valor inconsistente')

    def mostra_dados(self):
        print('- modelo:', self.modelo)
        print('ano:', self.marca)
        print('valor:', self.valor)

    def retorna_dados(self):
        print(f'{self.get_modelo()}, {self.get_marca()}, {self.get_valor()}')

    def aumento_valor(self, aumento):
        self.valor += aumento

if __name__ == '__main__':
    videogame1 = Videogame('Playstation 5', 'SONY', 5000.00)
    print('Objeto videogame1:', videogame1)

    videogame2 = Videogame('Xbox Series X', 'Microsoft')
    print('Objeto videogame2:', videogame2)

    videogame3 = Videogame('Megadrive')
    print('Obejto videogame3:', videogame3)

    print(videogame1.get_modelo())
    print(videogame1.get_marca())
    print(videogame1.get_valor())

    print(videogame2.get_modelo())
    print(videogame2.get_marca())
    print(videogame2.get_valor())

    print(videogame3.get_modelo())
    print(videogame3.get_marca())
    print(videogame3.get_valor())

    videogame1.set_modelo('Nintendo switch')
    videogame1.set_marca('Nintendo')
    videogame1.set_valor(3500.00)

    videogame2.set_modelo('Steam Deck')
    videogame2.set_marca('Valve')
    videogame2.set_valor(4000.00)

    videogame3.set_modelo('Atari')
    videogame3.set_marca('Atari')
    videogame3.set_valor(1000.00)

    print(videogame1.get_modelo())
    print(videogame1.get_marca())
    print(videogame1.get_valor())

    print(videogame2.get_modelo())
    print(videogame2.get_marca())
    print(videogame2.get_valor())

    print(videogame3.get_modelo())
    print(videogame3.get_marca())
    print(videogame3.get_valor())

    aumento_v = float(input('Digite o aumento do valor: '))

    videogame1.aumento_valor(aumento_v)
    print(videogame1.get_valor())

    videogame1.retorna_dados()
    videogame2.retorna_dados()
    videogame3.retorna_dados()