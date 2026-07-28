import functions
import interface
import sqlite3
from rich.console import Console
from pathlib import Path
console = Console()

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "faltas.db"

conexao1 = sqlite3.connect(DB_PATH)
cursor1 = conexao1.cursor()
functions.criar_tabela_materias(cursor=cursor1)
conexao1.commit()

while True:
    console.clear()
    opcao_escolhida = interface.criar_menu(txt="CONTROLE DE FALTAS V2")
    try:
        if opcao_escolhida == 1:
            resposta = True
            while resposta:
                conexao1.commit()
                console.clear()
                functions.ver_materias_e_faltas(cursor=cursor1)
                functions.registrar_materia(cursor=cursor1)
                conexao1.commit()
                console.clear()
                functions.ver_materias_e_faltas(cursor=cursor1)
                resposta = interface.confirmar_resposta("Deseja adicionar mais matérias? [S/N]: ")

        elif opcao_escolhida == 2:
            resposta = True
            while resposta:
                conexao1.commit()
                console.clear()
                functions.ver_materias_e_faltas(cursor=cursor1)
                functions.alterar_materia(cursor=cursor1)
                conexao1.commit()
                console.clear()
                functions.ver_materias_e_faltas(cursor=cursor1)
                resposta = interface.confirmar_resposta("Deseja alterar mais matérias? [S/N]: ")

        elif opcao_escolhida == 3:
            console.clear()
            functions.ver_materias_e_faltas(cursor=cursor1)
            input("Digite qualquer tecla para continuar: ")

        elif opcao_escolhida == 4:
            resposta = True
            while resposta:
                conexao1.commit()
                console.clear()
                functions.ver_materias_e_faltas(cursor=cursor1)
                functions.registrar_falta(cursor=cursor1)
                conexao1.commit()
                console.clear()
                functions.ver_materias_e_faltas(cursor=cursor1)
                resposta = interface.confirmar_resposta("Deseja registrar mais faltas? [S/N]: ")

        elif opcao_escolhida == 5:
            console.clear()
            functions.apagar_todos_dados(cursor=cursor1)
        
        elif opcao_escolhida == 6:
            console.clear()
            break
    except Exception as e:
        print(f"Ocorreu um erro : {e}")
        break
    else:
        conexao1.commit()
    print("\n"*10)

console.clear()
print("Tchau, até mais!")
conexao1.close()