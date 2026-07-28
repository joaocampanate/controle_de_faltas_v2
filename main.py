from functions import *
from interface import *
from classes import *
import sqlite3

conexao = sqlite3.connect('data/faltas.db')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Materias (
id INTEGER PRIMARY KEY,
nome_materia TEXT NOT NULL,
qtd_faltas INTEGER NOT NULL,
lim_faltas INTEGER NOT NULL);''')

while True:
    opcao_escolhida = criarmenu("CONTROLE DE FALTAS V2")
    try:
        if opcao_escolhida == 1:
            materia = inserir_materia()
            cursor.execute("INSERT INTO Materias (nome_materia,qtd_faltas,lim_faltas) VALUES (?,?,?)",(materia.nome,materia.faltas,materia.lim_faltas))
            print("Matéria adicionada!")

        elif opcao_escolhida == 2:
            continue

        elif opcao_escolhida == 3:
            continue

        elif opcao_escolhida == 4:
            continue

        elif opcao_escolhida == 5:
            continue
        
        elif opcao_escolhida == 6:
            break
    except Exception as e:
        print("Ocorreu um erro : {e}")
    else:
        conexao.commit()
print("Tchau, até mais!")