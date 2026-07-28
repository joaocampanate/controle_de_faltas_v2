import functions
import interface
import sqlite3

conexao1 = sqlite3.connect('data/faltas.db')
cursor1 = conexao1.cursor()
functions.criar_tabela_materias(cursor=cursor1)
conexao1.commit()

while True:
    opcao_escolhida = interface.criarmenu("CONTROLE DE FALTAS V2")
    try:
        if opcao_escolhida == 1:
            functions.registrar_materia(cursor=cursor1)

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