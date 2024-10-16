import mysql.connector
conexao = mysql.connector.connect(user='root',
                                   password='',
                                   host='127.0.0.1')
print('conexão:',conexao)
cursor_db = conexao.cursor()
sql = "CREATE DATABASE if not exists db_loja"
cursor_db.execute(sql)
cursor_db.close()
conexao.close()
print('\nconexão fechada')