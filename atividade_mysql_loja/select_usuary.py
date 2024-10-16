import mysql.connector
conexao = mysql.connector.connect(user='root',
                                password='',
                                host='127.0.0.1',
                                database = 'db_loja')

print('conexão:',conexao)
cursor = conexao.cursor()
pesquisa = input('Nome: ')
sql = f''' select * from tb_produto where nome like '%{pesquisa}%' '''
cursor.execute(sql)
l_registros = cursor.fetchall()
print('Registros da coluna:', cursor.rowcount)
print('-list of tuplas:')
print(l_registros)
print('-tuplas:')
for registro in l_registros:
    print(registro)
cursor.close()
conexao.close()