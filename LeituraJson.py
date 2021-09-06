import json

def LerJson(arquivo):
    
    # load: Carregar arquivo
    with open(arquivo, 'r') as file:
        json_data = json.dumps(json.load(file), indent=4)

    # loads: Carregar arquivo em uma lista de objetos
    print(json.loads(json_data))
    return json.loads(json_data)
# ReadJson