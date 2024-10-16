import mysql.connector
conexao = mysql.connector.connect(user='root',
                                password='',
                                host='127.0.0.1',
                                database = 'db_loja')

print('conexão:',conexao)
cursor = conexao.cursor()

sql = " select * from tb_produto "
cursor.execute(sql)
l_registros = cursor.fetchall()
print('- list of Tuplas:')
for registro in l_registros:  #imprime na vartical
    print(registro)
cursor.close()
conexao.close()
print('\nConexão Fechada.')