from time import sleep
from interface import leia_int_positivo, alterar_materia_opcoes, confirmar_resposta, cabecalho
from rich.table import Table
from rich.console import Console
console = Console()

def criar_tabela_materias(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Materias (
    id INTEGER PRIMARY KEY,
    nome_materia TEXT NOT NULL UNIQUE,
    qtd_faltas INTEGER NOT NULL,
    lim_faltas INTEGER NOT NULL);''')


def inserir_materia():
    nome_materia = str(input("Digite o nome da matéria: "))
    sleep(0.7)
    limite_faltas = leia_int_positivo("Digite o limite de faltas da matéria: ")
    sleep(0.7)
    return [nome_materia,0,limite_faltas]

def existe_alguma_materia(cursor):
    cursor.execute(
        "SELECT 1 FROM Materias;"
    )
    return cursor.fetchone() is not None

def materia_existe_nome(cursor, materia):
    cursor.execute(
        "SELECT 1 FROM Materias WHERE nome_materia = ?;",
        (materia,)
    )
    return cursor.fetchone() is not None

def materia_existe_id(cursor, id):
    cursor.execute(
        "SELECT 1 FROM Materias WHERE id = ?;",
        (id,)
    )
    return cursor.fetchone() is not None

    # Opções do menu

def registrar_materia(cursor):

    cabecalho("REGISTRO DE MATÉRIAS")
    materia = inserir_materia()
    if not materia_existe_nome(cursor, materia[0]):
        cursor.execute("INSERT INTO Materias (nome_materia,qtd_faltas,lim_faltas) VALUES (?,?,?);",(materia[0],materia[1],materia[2]))
        print("Operação solicitada com sucesso!")
        sleep(0.5)
    else:
        print("Essa matéria já existe no sistema! (use a opção de ALTERAR MATÉRIA caso queira ALTERAR algum dado sobre a matéria.)")
        sleep(0.5)


def alterar_materia(cursor):

    cabecalho("ALTERAÇÃO DE MATÉRIA REGISTRADA")
    id = leia_int_positivo("Digite o id da matéria que deseja alterar: ")
    if materia_existe_id(cursor, id):
        opcao = alterar_materia_opcoes()
        if opcao == 1:
            novo_nome = str(input("Digite o novo nome: "))
            sleep(0.3)
            if not materia_existe_nome(cursor, novo_nome):
                cursor.execute("UPDATE Materias SET nome_materia = ? WHERE id = ?;",(novo_nome,id))
                print("Operação solicitada com SUCESSO!")
            else:
                print("Esse nome já existe!")

        elif opcao == 2:
            nova_qtd = leia_int_positivo("Digite a nova quantidade de faltas: ")
            sleep(0.3)
            cursor.execute("UPDATE Materias SET qtd_faltas = ? WHERE id = ?;",(nova_qtd,id))
            print("Operação solicitada com SUCESSO!")

        elif opcao == 3:
            novo_lim = leia_int_positivo("Digite o novo limite de faltas: ")
            sleep(0.3)
            cursor.execute("UPDATE Materias SET lim_faltas = ? WHERE id = ?;",(novo_lim,id))
            print("Operação solicitada com SUCESSO!")

        elif opcao == 4:
            opcao = confirmar_resposta("Tem certeza que deseja apagar a matéria? [S/N]: ")
            sleep(0.3)
            if opcao:
                cursor.execute("DELETE FROM Materias WHERE id = ?;",(id,))
                print("MATÉRIA APAGADA!")
                sleep(0.3)
            else:
                print("OPERAÇÃO CANCELADA!")
                sleep(0.7)

    else:
        print('Este id não corresponde a nenhuma matéria.')
    sleep(0.3)


def ver_materias_e_faltas(cursor):
    cursor.execute("SELECT * FROM Materias")
    linhas = cursor.fetchall()
    tabela = Table(title='Matérias')
    tabela.add_column("ID",justify="center",style="blue")
    tabela.add_column("NOME",justify="center",style="cyan")
    tabela.add_column("FALTAS",justify="center",style="green")
    tabela.add_column("LIMITE",justify="center",style="red")
    for l in linhas:
        row = (str(l[0]), str(l[1]), str(l[2]), str(l[3]))
        tabela.add_row(*row)
    console.print(tabela)

def registrar_falta(cursor):

    cabecalho("REGISTRO DE FALTAS")
    id = leia_int_positivo("Digite o id da matéria que deseja registrar faltas: ")
    sleep(0.7)
    if materia_existe_id(cursor, id):
        faltas = leia_int_positivo("Quantas faltas deseja registrar?: ")
        sleep(0.6)
        cursor.execute("UPDATE Materias SET qtd_faltas = qtd_faltas + ? WHERE id = ?;",(faltas,id))
        print("Operação solicitada com SUCESSO!")
    else:
        print("Este id não corresponde a nenhuma matéria.")
    sleep(0.6)

def apagar_todos_dados(cursor):
    cabecalho("ELIMINAÇÃO DE DADOS")
    opcao = confirmar_resposta("Tem certeza que deseja apagar TODOS os dados? [S/N]: ")
    sleep(0.5)
    if opcao:
        cursor.execute("DELETE FROM Materias;")
        print("DADOS APAGADOS!")
        sleep(2)
    else:
        print("OPERAÇÃO CANCELADA!")
        sleep(1.5)
    
