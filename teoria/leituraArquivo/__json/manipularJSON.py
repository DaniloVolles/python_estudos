import json

# Encoding utf8 -> Se você omitir esse argumento, vai aparecer tudo desformatado.
# r+ --> Funciona ifual no "abrir arquivo", ver exemplos já organizados.
with open("exemplo.json", "r+", encoding="utf-8") as arquivo_json:
    objeto_json = json.load(arquivo_json) # Esse arquivo entra no python como um "dict"

# DICT:
# É um tipo de dado semelhante ao JSON, vc guarda esses dados com uma estrutura de chave/valor

print(type(objeto_json))
print(objeto_json)

print(objeto_json[2])

for i in objeto_json:
    print(i)

for i in objeto_json:
    print(i["nome"], "tem", i["idade"], "anos.")

