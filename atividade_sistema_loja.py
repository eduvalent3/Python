'''
1- Crie a classe Cliente e o construtor com os atributos (características): cpf e nome
2- Crie alguns métodos gets e sets. E o método __str__, teste.
3- Crie a classe CarrinhoCompra com os atributos: número do pedido, o cliente e os produtos
4- Crie alguns métodos gets e sets, teste
5- Crie a classe Produto com os atributos: identificador, nome, preço e quantidade.
6- Crie alguns métodos gets e sets, teste.
7- Crie o método __str__ pra retornar todos os dados de um produto formatados (concatenados)
8- Na classe CarrinhoCompra, crie o método para mostrar o nome do cliente
9- Crie o método mostra carrinho, mostre o nome dos produtos dentro do carrinho.
   Se o carrinho estiver vazio, mostre a mensagem "Carrinho vazio". Teste
10- Insira um produto no carrinho de compras do cliente1. Crie o método insere_produto,
    ele recebe um objeto da classe Produto e insere no carrinho.
11- Insira mais um produto no carrinho de compras do cliente1, teste
12- Crie o método mostra_carrinho2, com todos os dados do produto e a quantidade de itens
    no carrinho. Se o carrinho estiver vazio, mostre a mensagem "Carrinho vazio". Teste
13- Crie o método calcula_total, ele calcula o valor total da compra, ou seja,
    dos produtos no carrinho de compras, teste (valor total: 57,00)
14- Crie o método remova_produto, ele remove um produto do carrinho de compras, teste
15- Crie o método remova_produto2, ele remove um produto do carrinho de compras
    com críticas e mensagens, ou seja, verifica se o produto está no carrinho, teste
16- Insira mais um produto no carrinho de compras do cliente1, teste
17- Crie o método fecha compra. Ele finalize a compra e mostra os produtos e o
    valor total da compra, teste
'''
class Cliente(object):
    def __init__(self, cpf = 00000000000, nome = 'default'):
        self.cpf = cpf
        self.nome = nome

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def __str__(self):
        return (f'''
        Nome: {self.cpf}
        CPF: {self.nome}''')

class Produto(object):
    def __init__(self, identificador, nome_produto, preço, quantidade):
        self.identificador = identificador
        self.nome_produto = nome_produto
        self.preço = preço
        self.quantidade = quantidade

    def __str__(self):
        return (f'''
        Identificador: {self.identificador}
        Nome do Produto: {self.nome_produto}
        Preço: {self.preço}
        Quantidade de Produtos: {self.quantidade}''')

    def set_identificador(self, novo_identificador):
       self.identificador = novo_identificador

    def get_nome_produto(self):
        return self.nome_produto
    def set_nome_produto(self, novo_nome_produto):
        self.nome_produto = novo_nome_produto

    def set_preço(self, novo_preço):
        self.preço = novo_preço

    def set_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

class CarrinhoCompra(object):
    def __init__(self, numero_pedido, cliente):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.l_produtos = list()

    def set_numero_pedido(self, novo_numero):
        self.numero_pedido = novo_numero

    def set_cliente(self, novo_cliente):
        self.cliente = novo_cliente

    def __str__(self):
        return (f'''
        Número do Pedido: {self.numero_pedido}
        Cliente: {self.cliente}
        Lista de Produtos: {self.l_produtos}
''')

    def mostra_carrinho(self):
        if len(self.l_produtos) == 0:
            print('O seu carrinho está vazio!!!')
        else:
            for produto in self.l_produtos:
                print(produto.get_nome_produto())

    def insere_produto(self, produto):
        self.l_produtos.append(produto)

    def mostra_carrinho2(self):
        if len(self.l_produtos) == 0:
            print('O seu carrinho está vazio!!!')
        else:
            for produto in self.l_produtos:
                print(produto.__str__())

    def calcula_total(self):
        if len(self.l_produtos) == 0:
            print('O seu carrinho está vazio!!!')
        else:
            valor = 0
            for produto in self.l_produtos:
                valor += produto.get_preço() * produto.get_quantidade()
            print('O valor total é:', valor)

    def remova_produto(self, objeto):
        self.l_produtos.remove(objeto)

    def remova_produto2(self, objeto):
        if objeto in self.l_produtos:
            self.l_produtos.remove(objeto)
        else:
            print('Este produto não está no carrinho')

    def fecha_compra(self):
        return (f'''
        Lista de Produtos: {self.mostra_carrinho()}
        Valor Total: {self.calcula_total()}''')

if __name__ == '__main__':
    cliente1 = Cliente('123')
    print(cliente1)

    cliente2 = Cliente('223', 'Ailton')
    print(cliente2)

    produto1 = Produto(1234, 'Xbox', 1200, 1)

    carrinho1 = CarrinhoCompra(1234, cliente1)
    carrinho1.insere_produto(produto1)
    carrinho1.mostra_carrinho()

    carrinho1.mostra_carrinho2()

    carrinho1.remova_produto(produto1)
    carrinho1.mostra_carrinho()