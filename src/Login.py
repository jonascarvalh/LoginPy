from src.Diretorio   import LimparTerminal
from src.Diretorio   import ChaveProcurada
from src.LeituraJson import LerJson

def EfetuarLogin(login,senha):
    dados = LerJson()

    if ChaveProcurada(login,dados) == 0:
        LimparTerminal()
        print('Este usuário não existe!\n')
        return
    elif ChaveProcurada(login,dados) != senha:
        LimparTerminal()
        print('Senha inválida, tente novamente!\n')
    else:
        LimparTerminal()
        print('Você foi autenticado!\n')
    # Condicional: Chave Procurada
# EfetuarLogin