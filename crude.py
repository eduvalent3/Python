import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user='root',
                                         password='',
                                         host='127.0.0.1')

    print('Conexão db:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = "CREATE DATABASE if not exists db_loja_3"
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')

def create_connection():
    conexao  = mysql.connector.connect(user='root',
                                         password='',
                                         host='127.0.0.1',
                                         database='db_loja_3')

    print('Conexão:', conexao)
    return conexao

def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão Fechada')

def create_table():
    tabela = '''CREATE TABLE if not exists produto(
    identificador INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50),
    preco DECIMAL(9, 2) NOT NULL,
    dt_validade DATE NOT NULL,
    PRIMARY KEY (identificador))'''

    cursor.execute(tabela)

def insert_table():
    nome = input('Digite o nome do Produto: ')
    preco = float(input('Digite o preço do produto: '))
    dt_validade = input('Digite a data de validade aaaa-mm-dd: ')

    inserir = f'''INSERT INTO produto (nome, preco, dt_validade)
    VALUES('{nome}', {preco}, '{dt_validade}')'''

    cursor.execute(inserir)
    conexao.commit()

if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    insert_table()


    close_connection()
