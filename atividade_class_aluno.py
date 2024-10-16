class AlunoCeub:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome                                  #atributos
        self.mensalidade = mensalidade                    #self.nome_atributo = parametro
        self.idade = idade

    def get_nome(self):
        return self.nome

    def set_nome(self, nome_do_novo_aluno):
        self.nome = nome_do_novo_aluno

    def get_mensalidade(self):
        return self.mensalidade

    def set_mensalidade(self, valor):
        self.mensalidade = valor

    def get_mostrar_dados(self):
        return self.nome, self.idade, self.mensalidade

    def set_aumento_mensalidade(self, AumentoMensalidade):
        self.mensalidade = AumentoMensalidade + self.mensalidade

    def set_aumento_mensalidade_porcentagem(self, AumentoMensalidadePorcentagem):
        self.mensalidade = AumentoMensalidadePorcentagem/100 * self.mensalidade + self.mensalidade

    def pode_cnh(self):
        if self.idade >= 18:
            print('Você pode tirar a CNH!')
        else:
            print('Você não pode tirar a CNH!')



if __name__ == '__main__':
    aluno1 = AlunoCeub('Paulo', 1100.00, 17)
    print(aluno1)
    aluno2 = AlunoCeub('Carla', 900.00, 20)
    print(aluno2)
    print("- Aluno 1:")
    print("Nome:", aluno1.get_nome())
    print("- Aluno 2:")
    print(f"Nome: {aluno2.get_nome()}")
    novo_nome = input('Digite um novo nome: ')
    aluno1.set_nome(novo_nome)
    print(aluno1.get_nome())
    print(aluno1.get_mostrar_dados())
    aluno1.pode_cnh()