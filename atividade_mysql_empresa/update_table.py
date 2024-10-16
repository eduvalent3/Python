import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1',
                                  database='db_empresa')

print('Conexão:', conexao)
cursor = conexao.cursor()

sql = ('''update tb_funcionario 
        set salario = 7500.00
        where salario = 5500.00 ''')

cursor.execute(sql)
print('Registros Atulizados:', cursor.rowcount)
conexao.commit()
cursor.close()
conexao.close()