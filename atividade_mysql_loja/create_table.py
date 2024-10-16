import mysql.connector
conexao = mysql.connector.connect(user='root',
                                    password='',
                                    host='127.0.0.1',
                                    database = 'db_loja')
print('conexão:',conexao)
cursor = conexao.cursor()
sql = '''CREATE TABLE tb_produto(
    idt int NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL UNIQUE,
    preco DECIMAL(9, 2) NOT NULL,
    dta_validade DATE NULL,
    PRIMARY KEY (idt) )'''

cursor.execute(sql)
cursor.close()
conexao.close()
print('Conexão fechada')