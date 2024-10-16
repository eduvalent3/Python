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
    tabela = '''CREATE TABLE if not exists tb_cliente(
    identificador INTEGER NOT NULL AUTO_INCREMENT,
    cliente VARCHAR(80) NOT NULL,
    cpf CHAR(11) NOT NULL,
    endereco VARCHAR(100) NULL,
    dt_nascimento DATE NOT NULL,
    PRIMARY KEY (identificador))'''

    cursor.execute(tabela)

def insert_table():
    cliente = input('Digite o seu nome completo: ')
    cpf = input('Digite o seu CPF: ')
    endereco = input('Digite o seu endereço: ')
    dt_nascimento = input('Digite sua data de nascimento aaaa-mm-dd: ')

    inserir = f'''INSERT INTO tb_cliente (cliente, cpf, endereco, dt_nascimento)
    VALUES('{cliente}', '{cpf}', '{endereco}', '{dt_nascimento}')'''

    cursor.execute(inserir)
    conexao.commit()

def select_all():
    selecionar = 'select * from tb_cliente'
    cursor.execute(selecionar)
    l_registros = cursor.fetchall()
    if len(l_registros) > 0:
        for registro in l_registros:
            print('Primary Key:', registro[0])
            print('Cliente:', registro[1])
            print('CPF:', registro[2])
            print('Endereço:', registro[3])
            print('Data de Nascimento:', registro[4])
            print('-'*20)

if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    insert_table()
    select_all()

    while True:
        print("\nMENU:")
        print("[1] Para criar um novo registro")
        print("[2] Para listar registros")
        print("[3] Para sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            create_table()
            insert_table()
        elif opcao == "2":
            select_all()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")   

    close_connection(cursor, conexao)
