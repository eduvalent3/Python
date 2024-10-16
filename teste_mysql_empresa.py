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
    conexao = mysql.connector.connect(user='root',
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
    sql_cargo = """CREATE TABLE IF NOT EXISTS tb_cargo(
    idt INT NOT NULL AUTO_INCREMENT,
    cargo VARCHAR(45) UNIQUE NOT NULL,
    PRIMARY KEY (idt)
    )"""
    cursor.execute(sql_cargo)

    sql_empregado = """CREATE TABLE IF NOT EXISTS tb_empregado(
    idt INT NOT NULL AUTO_INCREMENT,
    empregado VARCHAR(45) NOT NULL,
    data_nascimento date NULL,
    genero ENUM('M', 'F') NOT NULL,
    cod_cargo int NOT NULL,
    PRIMARY KEY (idt),
    FOREIGN KEY(cod_cargo) REFERENCES tb_cargo(idt)
    )"""
    cursor.execute(sql_empregado)

def insert_cargo():
    cargo = input('Digite o nome do Cargo: ')

    inserir_cargo = f'''INSERT INTO tb_cargo (cargo)
    VALUES('{cargo}')'''

    cursor.execute(inserir_cargo)
    conexao.commit()

def insert_empregado():

    empregado = input('Digite o seu nome completo: ')
    data_nascimento = input('Digite sua data de nascimento aaaa-mm-dd: ')
    genero = input('Digite seu Gênero [M]Masculino e [F]Feminino: ')
    cod_cargo = input('Digite o código do cargo: ')

    inserir_empregado = f'''INSERT INTO tb_empregado (empregado, data_nascimento, genero, cod_cargo)
    VALUES('{empregado}', '{data_nascimento}', '{genero}', {cod_cargo})'''

    cursor.execute(inserir_empregado)
    conexao.commit()

def select_all():
    selecionar = 'select * from tb_empregado'
    cursor.execute(selecionar)
    l_registros = cursor.fetchall()
    if len(l_registros) > 0:
        for registro in l_registros:
            print('Primary Key:', registro[0])
            print('Empregado:', registro[1])
            print('Data de Nascimento:', registro[2])
            print('Genero:', registro[3])
            print('Código do Cargo:', registro[4])
            print('-' * 20)

def delete_empregado():
    nome = input('Digite o nome do empregado a ser deletado: ')
    delete = f'''delete from tb_empregado where empregado = '{nome}' '''

    cursor.execute(delete)
    conexao.commit()

def menu():
    while True:
        print("\nMENU:")
        print("[1] Para Criar um Cargo novo")
        print("[2] Para Criar um Registro de empregado")
        print("[3] Para mostrar todos os Registros de Empregados")
        print("[4] Para Deletar um Empregado")
        print("[0] Para Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            insert_cargo()
        elif opcao == "2":
            insert_empregado()
        elif opcao == "3":
            select_all()
        elif opcao == "4":
            delete_empregado()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    menu()

    close_connection()
