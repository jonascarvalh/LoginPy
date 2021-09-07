# Verifica se a chave procurada existe
def ChaveProcurada (chave, dados):
    for i in range(len(dados)):
        if chave in dados[i]['e-mail']:
            return dados[i]['senha']
        # if
    # for

    return 0
# ChaveProcurada