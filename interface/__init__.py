from time import sleep

def cabecalho(txt):

    print('-='*30)
    print(f'{txt:^40}')
    print('-='*30)

def leiaInt(msg = ''):

    while True:
        n = str(input(msg))
        try:
            int(n)
        except:
            print('Valor inválido.')
            continue
        else:
            return int(n)

def criarmenu(txt):

    cabecalho(txt)
    sleep(0.2)
    cont = 0

    opcoes = ['Adicionar matéria', 'Alterar matéria','Ver faltas e matérias', 'Registrar faltas', 'Apagar todos os dados', 'Sair do programa']

    for e in opcoes:
        cont +=1
        print(f'{cont} - {e}')
        sleep(0.2)

    print('-'*20)
    opcao = leiaInt('Opção selecionada: ')
    print('-'*20)
    sleep(0.2)

    while opcao not in range(1, cont+1):
        opcao = leiaInt('Opção inválida. Digite novamente: ')

    return opcao

def alterar_materia_opcoes():

    cont = 0

    opcoes = ['Alterar nome', 'Alterar quantidade de faltas','Alterar limite de faltas', 'Voltar']

    for e in opcoes:
        cont +=1
        print(f'{cont} - {e}')
        sleep(0.2)

    print('-'*20)
    opcao = leiaInt('Opção selecionada: ')
    print('-'*20)
    sleep(0.2)

    while opcao not in range(1, cont+1):
        opcao = leiaInt('Opção inválida. Digite novamente: ')

    return opcao

def confirmarResposta(msg):
    resposta = str(input(msg)).upper().strip()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Resposta inválida. Tente novamente: ')).upper().strip()
    if resposta == 'S':
        return True
    else:
        return False