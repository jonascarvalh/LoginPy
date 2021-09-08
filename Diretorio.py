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

# Define o nome do arquivo Json
def NomeArquivo():
    arquivo = 'dados.json'
    return arquivo
# NomeArquivo

# Verifica se a chave procurada existe
def ChaveProcurada (chave, dados):
    for i in range(len(dados)):
        if chave in dados[i]['e-mail']:
            return dados[i]['senha']
        # if
    # for

    return 0
# ChaveProcurada