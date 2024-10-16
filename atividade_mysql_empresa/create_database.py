import mysql.connector
conexao_db = mysql.connector.connect(user='root',
                                     password='',
                                     host='127.0.0.1')

print('Conexão:', conexao_db)
cursor_db = conexao_db.cursor()
sql = "CREATE DATABASE if not exists db_empresa"
cursor_db.execute(sql)
cursor_db.close()
conexao_db.close()

print('\nConexão Fechada!')