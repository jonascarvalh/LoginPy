import os

def ArquivoExiste(arquivo):
    if not os.path.isfile(arquivo):
        return True
    else:
        return False
# ArquivoExiste

def LimparTerminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
# LimparTerminal