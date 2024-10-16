'''
1- Crie o arquivo .py e a classe Produto.
2- O construtor da classe com os atributos: nome, vlr_compra, vlr_venda,
   qtd_estoque, qtd_minima
3- No main, crie o primeiro objeto da classe com os dados. Teste
4- Crie os métodos gets e sets dos atributos: nome, qtd_estoque e qtd_minima. Teste.
5- Altere a quantidade minima para um valor digitado. Teste.
6- Faça pelo menos uma crítica nos métodos set_qtd_estoque e set_nome. Teste.
7- Crie (acrescente) o método set_vlr_compra com crítica. Teste
8- Sobrescreva o método __str__ . Ele não recebe nada e retorna todos os atributos. Teste.
9- Crie o método funcional lucro. Não recebe nada e retorna o valor do lucro do produto. Teste
10- Crie o método funcional atualiza_estoque. Ele recebe a quantidade vendida
    de produtos e atualiza o estoque. Ele não retorna nada, teste
11- Método funcional repor_produto. Recebe a quantidade adquirida de produtos e atualiza, teste
12- Crie o método alerta_estoque. Não recebe nada e retorna um valor booleano. Retorna True,
   se a quantidade em estoque for menor que a quantidade mínima. Senão, retorna False. Teste
13- Crie o segundo objeto da classe passando apenas o argumento nome do produto, teste
14- No main, crie mais um objeto da classe passando apenas o argumento nome
    e valor de compra. Teste
15- No main, crie mais um objeto da classe passando apenas o argumento nome e
    a quantidade em estoque. Teste
16- Crie o método maior_qtd, ele compara dois produtos quaisquer e mostra
    o produto que tem a maior qtd em estoque. Teste

17- Crie o método maior_lucro, ele compara dois produtos quaisquer e mostra
    o produto que tem mais lucro.

18- O sistema precisa informar a quantidade de produtos cadastrados, ou seja,
    a quantidade de objetos criados. Teste
19- Crie o método de classe para retornar a quantidade de produtos cadastrados. Teste
'''

class Produto(object):
    ct = 0
    def __init__(self, nome = 'default', valor_de_compra = 0, valor_de_venda = 0, qtd_estoque = 0, qtd_minima = 0):
        self.nome = nome
        self.valor_de_compra = valor_de_compra
        self.valor_de_venda = valor_de_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima
        Produto.ct += 1

    def __str__(self):
        return(f'''
        nome: {self.nome}
        Valor de Compra: {self.valor_de_compra}
        Valor de Venda: {self.valor_de_venda}
        Quantidade do Estoque: {self.qtd_estoque}
        Quantidade Mínima do estoque: {self.qtd_minima}
''')

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if type(novo_nome) == str:
            self.nome = novo_nome
        else:
            print('Você digitou um nome inválido')

    def get_valor_de_compra(self):
        return self.valor_de_compra

    def get_valor_de_venda(self):
        return self.valor_de_venda

    def get_qtd_estoque(self):
        return self.qtd_estoque

    def set_qtd_estoque(self, nova_qtd_estoque):
        if type(nova_qtd_estoque) == int:
            self.qtd_estoque = nova_qtd_estoque
        else:
            print('Você não digitou um valor inteiro')

    def get_qtd_minima(self):
        return self.qtd_minima

    def set_qtd_minima(self, nova_qtd_minima = input('Digite uma nova quantidade mínima: ')):
        self.qtd_minima = nova_qtd_minima

    def lucro(self):
        return self.valor_de_venda - self.valor_de_compra

    def atualiza_estoque(self, qtd_vendida_produtos):
        self.qtd_estoque = self.qtd_estoque - qtd_vendida_produtos

    def repor_produtos(self, qtd_adquirida_produtos):
        self.qtd_estoque = self.qtd_estoque + qtd_adquirida_produtos

    def alerta_estoque(self):
        if self.qtd_estoque < self.qtd_minima:
            return True
        else:
            return False

    def maior_qtd(self, o_produto):
        if self.qtd_estoque > o_produto.qtd_estoque:
            return f'o primeiro produto tem {self.get_qtd_estoque()} de estoque e o segundo possui {o_produto.get_qtd_estoque()}'
        else:
            return 'O primeiro produto tem menos quantidade de estoque que o segundo'

    def maior_lucro(self, o_produto):
        if self.lucro() > o_produto.lucro():
            return f'O produto {self.nome} teve maior lucro que o produto {o_produto.nome}'
        else:
            return f'O produto {self.nome} teve menor lucro que o produto {o_produto.nome}'

if __name__ == '__main__':
    produto1 = Produto('Xbox Series X', 3000.00, 3700.00, 30, 5)
    print(f'O menu do produto 1 é: {produto1.__str__()}')

    produto2 = Produto('Xbox Series S')
    print(f'O menu do produto 2 é: {produto2.__str__()}')

    produto3 = Produto('Xbox One x', 1000.00)
    print(f'O menu do produto 3 é: {produto3.__str__()}')

    print(f'O lucro do produto 1 é: {produto1.lucro()} reais')

    produto1.atualiza_estoque(17)
    print(f'Seu estoque atualizado é: {produto1.get_qtd_estoque()}')

    produto1.repor_produtos(20)
    print(f'Após a reposição de produtos, seu novo estoque é de: {produto1.get_qtd_estoque()}')

    print(f'''Seu produto1 precisa ser reposto? {produto1.alerta_estoque()}
     seu estoque possui {produto1.get_qtd_estoque()} produtos e a quantidade mínima é de {produto1.get_qtd_minima()}''')

    produto1.maior_qtd(produto2)

    produto1.maior_lucro(produto2)

    print(f'Quantidade de produtos cadastrados {Produto.ct}')