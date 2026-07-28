from functions import *
from interface import *
from classes import *
import sqlite3

conexao = sqlite3.connect('data/faltas.db')
cursor = conexao.cursor()

opcao_escolhida = criarmenu("CONTROLE DE FALTAS V2")