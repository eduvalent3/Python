"""
Implemente:
1- Crie a classe Livro com os atributos: título, autor, páginas e preço.
2- Crie o método construtor (init) que recebe quatro parâmetros e
   use pelo menos um desses parâmetros com valor default (padrão)
3- Crie o objeto livro1 passando os quatro argumentos, teste
4- Crie o objeto livro2 passando apenas três argumentos, teste
5- Crie pelo menos um método get e pelo menos um método set, teste
6- No item anterior, faça crítica no método set, teste
7- Crie o método funcional aumento_preco com o objetivo de atualizar o preço do livro.
   Esse método recebe o valor do aumento e atualiza o atributo preco. Teste
8- Use (teste) todos os métodos criados na classe Livro para os objetos livro1 e livro2.
9- Crie o método mostra_dados, mostra todos os valores dos atributos
10- Crie o método funcional aumento_porcentagem para atualizar o preço
11- Crie o mètodo __str__
12- Elabore o enunciado de mais um método funcional importante para a classe

- O sistema precisa informar quantos livros foram cadastrados.
14- Crie o método de classe para recuperar essa informação

15- Armazene os livros criados (instanciados).
16- Crie o método para mostrar todos os livros cadastrados (instanciados).
- Acrescente o número do livro, a seguência.
18- Mostre os atributos de todos os livros."""

class Livro(object):
    def __init__(self, autor, pagina, preco, titulo = 'default'):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        if self.preco == type(str):
            return 'Você não digitou um valor válido'
        else:
            self.preco = novo_preco

    def aumento_preco(self, aumento):
        self.preco = self.preco + aumento

    def mostra_dados(self):
        return (f'''
        Titulo: {self.titulo}
        Autor: {self.autor}
        Páginas: {self.pagina}
        Preço: {self.preco}''')

    def aumento_porcentagem(self, porcentagem):
        self.preco = (self.preco * porcentagem)/100 + self.preco

    def __str__(self):
        return(f'''
        Titulo: {self.titulo}
        Autor: {self.autor}
        Páginas: {self.pagina}
        Preço: {self.preco}''')

if __name__ == '__main__':
    livro1 = Livro('Hobbit', 250, 50, 'Tolkien')
    print(f'O preço do livro 1 é: {livro1.get_preco()}')

    livro1.set_preco(80)
    print(f'O novo preço do livro 1 é: {livro1.get_preco()}')

    livro2 = Livro('Biblia', 9000, 80)
    print(f'O preço do Livro 2 é: {livro2.get_preco()}')

    livro2.aumento_preco(5)
    print(f'O novo valor com aumento do livro 2 é:{livro2.get_preco()}')

    print(livro2.mostra_dados())
