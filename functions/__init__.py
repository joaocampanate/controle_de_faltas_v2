from classes import *
from interface import leiaInt

def inserir_materia():
    nome_materia = str(input("Digite o nome da matéria: "))
    limite_faltas = leiaInt("Digite o limite de faltas da matéria: ")
    materia = Materia(nome_materia, 0, limite_faltas)
    return (materia)