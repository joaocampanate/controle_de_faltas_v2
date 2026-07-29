import time
from rich.table import Table

def cabecalho(txt):

    print('-='*30)
    print(f'{txt:^40}')
    print('-='*30)

def mensagem_nao_existe_materia():
    txt = "NENHUMA MATÉRIA REGISTRADA."
    print('-='*30)
    print(f'{txt:^40}')
    print('-='*30)
    time.sleep(2.5)

def mensagem_despedida():
    txt = "ADEUS, VOLTE SEMPRE!"
    print('-='*30)
    print(f'{txt:^40}')
    print('-='*30)
    time.sleep(2.5)

def leia_apenas_letras(msg = ''):
    MIN_CARACTER = 3
    MAX_CARACTER = 35
    while True:
        l = str(input(msg))
        if len(l) <= 25 and len(l) >= 3:
            if l.isalpha():
                return l
            else:
                print("Nome inválido, insira apenas letras. ")
                continue
        else:
            print(f"Nome inválido, a quantidade mínima de caracteres é {MIN_CARACTER} e a quantidade máxima é {MAX_CARACTER}.")

def leia_int_positivo(msg = ''):
    MAX_CARACTER = 4
    while True:
        n = str(input(msg))
        if len(n) <= MAX_CARACTER:
            try:
                n = int(n)
            except:
                print('Valor inválido.')
                continue
            else:
                if n >= 0:
                    return int(n)
        else:
            print(f"ERRO, número digitado excede o limite de caracteres: {MAX_CARACTER}")

def criar_menu(txt):

    cabecalho(txt)
    time.sleep(0.2)
    cont = 0

    opcoes = ['Adicionar matéria', 'Alterar ou excluir matéria','Ver faltas e matérias', 'Registrar faltas', 'Apagar todos os dados', 'Sair do programa']

    for e in opcoes:
        cont +=1
        print(f'{cont} - {e}\n')
        time.sleep(0.2)

    print('-'*20)
    opcao = leia_int_positivo('Opção selecionada: ')
    print('-'*20)
    time.sleep(0.2)

    while opcao not in range(1, cont+1):
        opcao = leia_int_positivo('Opção inválida. Digite novamente: ')

    return opcao

def alterar_materia_opcoes():

    cont = 0

    opcoes = ['Alterar nome', 'Alterar quantidade de faltas','Alterar limite de faltas', 'Excluir matéria', 'Voltar']

    for e in opcoes:
        cont +=1
        print(f'{cont} - {e}\n')
        time.sleep(0.6)

    print('-'*20)
    opcao = leia_int_positivo('Opção selecionada: ')
    print('-'*20)
    time.sleep(0.2)

    while opcao not in range(1, cont+1):
        opcao = leia_int_positivo('Opção inválida. Digite novamente: ')

    return opcao

def confirmar_resposta(msg):
    resposta = str(input(msg)).upper().strip()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Resposta inválida. Tente novamente: ')).upper().strip()
    if resposta == 'S':
        return True
    else:
        return False