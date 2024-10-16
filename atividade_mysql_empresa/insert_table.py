import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1',
                                  database='db_empresa')

print('Conexão:', conexao)
cursor = conexao.cursor()
sql = '''insert into tb_funcionario
        (idt, nome, salario)
        values
        (5, 'Kley', 1500.00),
        (6, 'Gabriel', 1600.00)'''

cursor.execute(sql)
conexao.commit()
print(cursor.rowcount, "record inserted.")
cursor.close()
conexao.close()
print('\nConexão Fechada.')