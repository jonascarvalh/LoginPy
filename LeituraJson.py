import json

def LerJson(arquivo):
    # load: Carregar arquivo
    # loads: Carregar arquivo em uma lista de objetos
    with open(arquivo, 'r') as file:
        json_data = json.loads(json.dumps(json.load(file), indent=4))
    #with

    '''
    # Percorrer a lista de objetos por uma key(e-mail)
    # Isso aqui vai servir depois confia
    if not json_data:
        print('vazio')
    else:
        for i in range (len(json_data)):
            print(json_data[i]['e-mail'])
    '''

    return json_data
# ReadJson