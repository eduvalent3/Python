import sqlite3
conexao = sqlite3.connect('Livraria.db')
cur = conexao.cursor()
sql = 'select * from tb_cliente'
cur.execute(sql)
l_registros = cur.fetchall()
#print(l_registros)
print('Consulta Todos:')
for registro in l_registros:
    print(registro)
cur.close()
conexao.close
print('Fechou a base de dados!!!')