import json
import csv

with open("nomes.json", "r") as arquivo:
    objeto_json = json.load(arquivo) #Carregar o arquivo como um objeto JSON
    nomes = objeto_json["nomes"]

with open("nomes.csv", "w") as arquivo:

    campos = nomes[0].keys() #Isso aqui passa as "chaves" de cada json como "cabeçalhos"
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader() #Isso aqui escreve o valor das chaves no "cabeçalho"

    for nome in nomes:
        escritor.writerow(nome) # Isso aqui escreve cada linha de nome/idade do json para CSV
