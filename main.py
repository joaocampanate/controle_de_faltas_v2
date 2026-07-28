from functions import *
from interface import *
import sqlite3

conexao = sqlite3.connect('data/faltas.db')
cursor = conexao.cursor()

criarmenu("CONTROLE DE FALTAS V2")