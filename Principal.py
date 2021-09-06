import sys
from EscritaJson import EscritaJson

def Cadastro():
    email = input('Indique seu e-mail: ')
    senha = input('Indique sua senha:  ')
    EscritaJson(email,senha)
# Cadastro

def Login():
    email = input('Indique seu e-mail: ')
    senha = input('Indique sua senha:  ')
# Login

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