import time
from rich import print

def cabecalho(txt):

    print('-='*30)
    print(f'[blue]{txt:^60}[/blue]')
    print('-='*30)

def mensagem_nao_existe_materia():
    txt = "NENHUMA MATÉRIA REGISTRADA."
    print('-='*30)
    print(f'[red]{txt:^40}[/red]')
    print('-='*30)
    time.sleep(2.5)

def mensagem_despedida():
    txt = "[green]            ADEUS, VOLTE SEMPRE! [/green]👋"
    print('-='*30)
    print(f'{txt:^60}')
    print('-='*30)
    time.sleep(2.5)

def msg_operacao_concluida():
    print("\n ✅  [green]OPERAÇÃO CONCLUÍDA[/green]  ✅")

def msg_operacao_cancelada():
    print("\n ❌️  [red]OPERAÇÃO CANCELADA[/red]  ❌️")

def msg_erro(txt= ''):
    print(f"\n ⛔  [red]{txt}[/red]  ⛔", end='   ')


def leia_apenas_letras(msg = ''):
    MIN_CARACTER = 3
    MAX_CARACTER = 30
    while True:
        l = str(input(msg))
        if l.find(' ') >= 1:
            lformat = l.replace(' ', '')
        else:
            lformat = l
        if lformat.isalpha():
            if len(l) >= 3 and len(l) <= 35:
                return l
            else:
                msg_erro(f"A quantidade mínima de caracteres é {MIN_CARACTER} e a quantidade máxima é {MAX_CARACTER}")
                continue
        else:
            msg_erro("Digite apenas letras")

def leia_int_positivo(msg = ''):
    MAX_CARACTER = 4

    while True:
        n = str(input(msg))
        if len(n) <= MAX_CARACTER:
            try:
                n = int(n)
            except:
                msg_erro("Digite apenas números inteiros")
                continue
            else:
                if n >= 0:
                    return int(n)
        else:
            msg_erro(f"O número digitado excede a quantidade máxima de caracteres suportados : {MAX_CARACTER}")

def criar_menu(txt):

    cabecalho(txt)
    time.sleep(0.2)
    cont = 0

    opcoes = ['Adicionar matéria', 'Alterar ou excluir matéria','Ver faltas e matérias', 'Registrar faltas', 'Apagar todos os dados', 'Sair do programa']

    for e in opcoes:
        cont +=1
        print(f'{cont} - [yellow]{e}[/yellow]\n')
        time.sleep(0.2)

    print('-'*20)
    opcao = leia_int_positivo('Opção selecionada: ')
    print('-'*20)
    time.sleep(0.2)

    while opcao not in range(1, cont+1):
        msg_erro("Opção inválida. Tente novamente: ")
        opcao = leia_int_positivo()

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
        msg_erro("Opção inválida. Tente novamente: ")
        opcao = leia_int_positivo()

    return opcao

def confirmar_resposta(msg):
    resposta = str(input(msg)).upper().strip()
    while resposta != 'S' and resposta != 'N':
        msg_erro("Opção inválida, tente novamente [S/N]: ")
        resposta = str(input('')).upper().strip()
    if resposta == 'S':
        return True
    else:
        return False