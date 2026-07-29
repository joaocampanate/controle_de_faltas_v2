from time import sleep
from interface import leia_int_positivo, alterar_materia_opcoes, confirmar_resposta, cabecalho, leia_apenas_letras, msg_operacao_concluida, msg_operacao_cancelada, msg_erro
from rich.table import Table
from rich.console import Console
from rich import print
console = Console()

def criar_tabela_materias(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Materias (
    id INTEGER PRIMARY KEY,
    nome_materia TEXT NOT NULL UNIQUE,
    qtd_faltas INTEGER NOT NULL,
    lim_faltas INTEGER NOT NULL);''')


def inserir_materia():
    nome_materia = leia_apenas_letras("\n\n Digite o nome da matéria que deseja registrar: ")
    sleep(0.7)
    limite_faltas = leia_int_positivo("\n\n Digite o limite de faltas da matéria: ")
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
        msg_operacao_concluida()
        sleep(0.5)
    else:
        msg_erro("Essa matéria ja foi registrada. (Use a opção de ALTERAR OU EXCLUIR MATERIA se quiser editá-la)")
        sleep(4.5)


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
                msg_operacao_concluida()
            else:
                msg_erro("Esse nome já está registrado em outra matéria")
                sleep(2)

        elif opcao == 2:
            nova_qtd = leia_int_positivo("\nDigite a nova quantidade de faltas: ")
            sleep(0.3)
            cursor.execute("UPDATE Materias SET qtd_faltas = ? WHERE id = ?;",(nova_qtd,id))
            msg_operacao_concluida()

        elif opcao == 3:
            novo_lim = leia_int_positivo("\nDigite o novo limite de faltas: ")
            sleep(0.3)
            cursor.execute("UPDATE Materias SET lim_faltas = ? WHERE id = ?;",(novo_lim,id))
            msg_operacao_concluida()

        elif opcao == 4:
            print("\n ⚠️ [red] Tem certeza que deseja apagar a matéria? [/red]⚠️  [S/N]: ", end='')
            opcao = confirmar_resposta("")
            sleep(0.3)
            if opcao:
                cursor.execute("DELETE FROM Materias WHERE id = ?;",(id,))
                msg_operacao_concluida()
                sleep(0.3)
            else:
                msg_operacao_cancelada()
                sleep(0.7)

    else:
        msg_erro("ID não encontrado")
    sleep(2)


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
        msg_operacao_concluida()
    else:
        msg_erro('ID não encontrado')
    sleep(3)

def apagar_todos_dados(cursor):
    cabecalho("ELIMINAÇÃO DE DADOS")
    print("⚠️ [red] Tem certeza que deseja apagar TODOS os dados? [/red]⚠️  [S/N]: ", end='')
    opcao = confirmar_resposta("")
    sleep(0.5)
    if opcao:
        cursor.execute("DELETE FROM Materias;")
        msg_operacao_concluida()
        sleep(2)
    else:
        msg_operacao_cancelada()
        sleep(1.5)
    
