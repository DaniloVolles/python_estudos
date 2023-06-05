# Escrever e manipular arquivos JSON com Python
import json

exemploStr = {
    "CIDADE": "BRASILIA",
    "ESTADO": "DF",
    "HABITANTES": 1000
}, {
    "CIDADE": "CURITIBA",
    "ESTADO": "PARANA",
    "HABITANTES": 2000
}

print(type(exemploStr))

object_json = json.dumps(exemploStr, indent=3)

with open("exemplo2.json", "w+", encoding="utf-8") as file:
    file.write(object_json)
