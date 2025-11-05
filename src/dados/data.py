import json


# Função que lê informações de json
def lerInfos (caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


# Função que escreve dados em um arquivo json
def escreverInfos (caminho, data):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo, indent=4, ensure_ascii=False)

usuarioLogado = []