import functions
import interface
import sqlite3
from pathlib import Path
from time import sleep

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "faltas.db"

conexao1 = sqlite3.connect(DB_PATH)
cursor1 = conexao1.cursor()
functions.criar_tabela_materias(cursor=cursor1)
conexao1.commit()

while True:
    opcao_escolhida = interface.criarmenu(txt="CONTROLE DE FALTAS V2")
    try:
        if opcao_escolhida == 1:
            functions.registrar_materia(cursor=cursor1)

        elif opcao_escolhida == 2:
            functions.ver_materias_e_faltas(cursor=cursor1)
            functions.alterar_materia(cursor=cursor1)

        elif opcao_escolhida == 3:
            functions.ver_materias_e_faltas(cursor=cursor1)

        elif opcao_escolhida == 4:
            functions.ver_materias_e_faltas(cursor=cursor1)
            functions.registrar_falta(cursor=cursor1)

        elif opcao_escolhida == 5:
            functions.apagar_todos_dados(cursor=cursor1)
        
        elif opcao_escolhida == 6:
            break
    except Exception as e:
        print(f"Ocorreu um erro : {e}")
    else:
        conexao1.commit()
    print("\n"*10)
print("Tchau, até mais!")