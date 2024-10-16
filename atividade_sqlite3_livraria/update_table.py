import sqlite3

conexao=sqlite3.connect('Livraria.db')
cur=conexao.cursor()

sql = "update tb_cliente set nome=? where cpf=?"

novo_nome = input('Digite o novo nome: ')
cpf_pesquisa = input('CPF de pesquisa: ')
cur.execute(sql, (novo_nome, cpf_pesquisa))

#cur.execute(sql, ('Carla', '1234'))

conexao.commit()
cur.close()
conexao.close()
print('Fechou a base de dados')