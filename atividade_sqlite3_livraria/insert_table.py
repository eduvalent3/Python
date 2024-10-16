import sqlite3
conexao = sqlite3.connect('Livraria.db')
cur = conexao.cursor()
sql = "Insert into tb_cliente(cpf, nome, idade) values ('1235', 'paula', 31)"
cur.execute(sql)
conexao.commit()
cur.close()
conexao.close()
print("Fechou a base de dados")