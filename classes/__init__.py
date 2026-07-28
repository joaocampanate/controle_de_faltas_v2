from interface import *
class Materia:
    def __init__(self, nome_materia, qtd_faltas, limite_faltas):
        self.nome = nome_materia
        self.faltas = qtd_faltas
        self.lim_faltas = limite_faltas

    def alterar_dados(self):
        print("O que deseja alterar?\n")
        opcao = leiaInt("1 - Nome\n2 - Quantidade de faltas\n3 - Limite de Faltas")
        if opcao == 1:
            self.nome_materia = str(input("Digite o novo nome: "))
        if opcao == 2:
            self.qtd_faltas = leiaInt("Digite a nova quantidade de faltas: ")
        if opcao == 3:
            self.limite_faltas = leiaInt("Digite o novo limite de faltas: ")