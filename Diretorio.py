import os

def ArquivoExiste(arquivo):
    if not os.path.isfile(arquivo):
        return True
    else:
        return False
# ArquivoExiste
