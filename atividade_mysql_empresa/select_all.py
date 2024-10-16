import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1',
                                  database='db_empresa')

print('Conexão:', conexao)
cursor = conexao.cursor()

sql = 'select * from tb_funcionario'
cursor.execute(sql)
l_registros = cursor.fetchall()
if len(l_registros) > 0:
    for registro in l_registros:
        print('Primary Key:', registro[0])
        print('Nome:', registro[1])
        print('Salário:', registro[2])
        print('-'*20)

else:
    print('Lista Vazia')

cursor.close()
conexao.close()