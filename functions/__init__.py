from classes import *
from interface import leiaInt

def inserir_materia():
    nome_materia = str(input("Digite o nome da matéria: "))
    limite_faltas = leiaInt("Digite o limite de faltas da matéria: ")
    materia = Materia(nome_materia, 0, limite_faltas)
    return (materia)

def materia_existe(cursor, materia):
    cursor.execute(
        "SELECT 1 FROM Materias WHERE nome_materia = ?;",
        (materia,)
    )
    return cursor.fetchone() is not None

def registrar_materia(cursor):
    materia = inserir_materia()
    if not materia_existe(cursor, materia.nome):
        cursor.execute("INSERT INTO Materias (nome_materia,qtd_faltas,lim_faltas) VALUES (?,?,?)",(materia.nome,materia.faltas,materia.lim_faltas))
        print("Matéria adicionada!")
    else:
        print("A matéria já existe!")