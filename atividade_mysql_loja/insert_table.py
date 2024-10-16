import mysql.connector
conexao = mysql.connector.connect(user='root',
                                password='',
                                host='127.0.0.1',
                                database = 'db_loja')

print('conexão:',conexao)
cursor = conexao.cursor()
nome = input('Nome: ')
preco = float(input('Preço: '))
data = input('Data: aaaa-mm-dd: ')
sql = f'''insert into tb_produto
        (nome, preco, dta_validade)
        values ('{nome}', {preco}, '{data}') '''

cursor.execute(sql)
conexao.commit()
cursor.close()
print('\nConexão Fechada.')