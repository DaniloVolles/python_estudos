import json

with open('nomes.json', encoding='utf-8') as arq_json:
    dados = json.loads(arq_json.read())
    pessoas_lista = dados ['pessoas']
    print(type(pessoas_lista))

    for p in pessoas_lista:
        p.update({'sobrenome':'Flores'})
        p.__setitem__("cpf","123.456.789-00")
        print(p)

# p é um dicionário, no caso, update() e __setitem__() são funções de dicionários
# Se fosse uma lista, a gente usaria o append() ou o insert()