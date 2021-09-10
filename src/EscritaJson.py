import json
import src.Diretorio   as Dir
from   src.LeituraJson import LerJson

def GerarJson(arquivo):
    dado = []
    Escrita(arquivo,dado)
# GerarJson

# Aplica a entrada em forma de Json
def ModeloVazio(login,senha):
    # Formato Json a ser escrito
    dado = [{ 
        "e-mail": login,
        "senha" : senha
    }]
    return dado
# Modelo

# Funcao escreve o dado quando o arquivo estiver vazio
def Escrita(arquivo, dado):
    # Escrever arquivo formatado
    with open(arquivo, 'w') as file:
        json.dump(dado,file,sort_keys=True,indent=4) # Escreve e formata o json
    # with
# Escrita

def ModeloNaoVazio(dados,login,senha):
    # Adicionando outro dado
    dados.append({
        "e-mail": login,
        "senha" : senha
    })
    return dados
# ModeloNaoVazio

def ObterChaveEmail(dados):
    return dados['e-mail']
# ObterChaveEmail

def EscritaJson (login,senha):
    # Recebe o nome do arquivo
    arquivo = Dir.CaminhoArquivo()

    # Verifica se o arquivo existe
    # Caso não exista, cria um novo
    if Dir.ArquivoExiste(arquivo):
        GerarJson(arquivo)
    # Arquivo Existe
    
    # Faz a leitura do arquivo em questão e 
    # retorna os elementos
    dados = LerJson()

    # Verifica se o login já existe, caso exista
    # não faz o cadastro
    if Dir.ChaveProcurada(login,dados) != 0:
        Dir.LimparTerminal()
        print('Este e-mail já está cadastrado\n')
        return 0
    # Chave Procurada

    # Monta o dado de acordo com o tipo Json
    # e insere esse dado
    # se estiver vazio, ou não
    if not dados:
        dados = ModeloVazio(login,senha)
        Escrita(arquivo,dados)
        Dir.LimparTerminal()
        print('Sua conta foi registrada com sucesso!\n')
    else:
        dados = ModeloNaoVazio(dados,login,senha)
        dados.sort(key=ObterChaveEmail)
        Escrita(arquivo,dados)
        Dir.LimparTerminal()
        print('Sua conta foi registrada com sucesso!\n')
    # if not
# WriteJson