import json
import csv

with open("layout.json", encoding="utf-8") as arq_json:
    dados = json.loads(arq_json.read())
    livros_lista = dados["livros"]

    print(type(livros_lista))

    linhas = []
    for livro in livros_lista:
        p = []
        p.append(livro["dados_cadastrais"]["id"])
        p.append(livro["dados_cadastrais"]["autor"])
        p.append(livro["dados_cadastrais"]["nome_livro"])
        p.append(livro["dados_cadastrais"]["data_publicacao"])
        print(p)

        linhas.append(p)

with open("extracao.csv", "x") as arquivo_csv:
    for livro in livros_lista:
        writer = csv.writer(arquivo_csv, delimiter=";")

    writer.writerows(linhas)
