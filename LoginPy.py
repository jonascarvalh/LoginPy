import sys
from   src.EscritaJson import EscritaJson
from   src.Diretorio   import LimparTerminal
from   src.Login       import EfetuarLogin

def Cadastro():
    LimparTerminal()
    print(' ==「 Cadastro 」== ')
    email = input('E-mail: ')
    senha = input('Senha:  ')
    EscritaJson(email,senha)
# Cadastro

def Login():
    LimparTerminal()
    print(' ==「 Login 」== ')
    email = input('E-mail: ')
    senha = input('Senha:  ')
    EfetuarLogin(email,senha)
# Login

LimparTerminal()
while(1):
    print('[1] Cadastro')
    print('[2] Login')
    print('[0] Sair')
    opcao = int(input('Indique a opcao desejada\n>>'))

    if (opcao == 1):
        Cadastro()
    elif (opcao == 2):
        Login()
    else:
        sys.exit()
# while