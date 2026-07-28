from functions import *
from interface import *
from classes import *
import sqlite3

conexao1 = sqlite3.connect('data/faltas.db')
cursor1 = conexao1.cursor()
criar_tabela_materias(cursor=cursor1)
conexao1.commit()

while True:
    opcao_escolhida = criarmenu("CONTROLE DE FALTAS V2")
    try:
        if opcao_escolhida == 1:
            registrar_materia(cursor=cursor1)

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
        print(f"Ocorreu um erro : {e}")
    else:
        conexao1.commit()
print("Tchau, até mais!")