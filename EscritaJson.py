import json
import os
from LeituraJson import LerJson

# Define o nome do arquivo Json
def NomeArquivo():
    arquivo = 'dados.json'
    return arquivo
# NomeArquivo

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
        json.dump(dado,file,indent=4) # Escreve e formata o json
    # with
# Escrita

def ModeloNaoVazio(dado,login,senha):
    # Adicionando outro dado
    dado.append({
        "e-mail": login,
        "senha" : senha
    })
    return dado
# ModeloNaoVazio

def EscritaJson (login,senha):
    # Gera arquivo json
    arquivo = NomeArquivo()

    if not os.path.isfile(arquivo):
        GerarJson(arquivo)
    # if

    # Faz a leitura do arquivo em questão e 
    # retorna os elementos caso exista
    dado = LerJson(arquivo)

    # Monta o dado de acordo com o tipo Json
    # Quando estiver vazio
    # Escreve o dado quando o Json está vazio
    if not dado:
        dado = ModeloVazio(login,senha)
        Escrita(arquivo,dado)
    else:
        dado = ModeloNaoVazio(dado,login,senha)
        Escrita(arquivo,dado)
    # if not
# WriteJson