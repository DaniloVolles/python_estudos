import pandas as pd
import jellyfish as jf
from unidecode import unidecode

def gerar_df_ibge():
    siglas_estados = {  # Se trata das siglas de todos os estados brasileiros
        "Rondônia": "RO",
        "Acre": "AC",
        "Amazonas": "AM",
        "Roraima": "RR",
        "Pará": "PA",
        "Amapá": "AP",
        "Tocantins": "TO",
        "Maranhão": "MA",
        "Piauí": "PI",
        "Ceará": "CE",
        "Rio Grande do Norte": "RN",
        "Paraíba": "PB",
        "Pernambuco": "PE",
        "Alagoas": "AL",
        "Sergipe": "SE",
        "Bahia": "BA",
        "Minas Gerais": "MG",
        "Espírito Santo": "ES",
        "Rio de Janeiro": "RJ",
        "São Paulo": "SP",
        "Paraná": "PR",
        "Santa Catarina": "SC",
        "Rio Grande do Sul": "RS",
        "Mato Grosso do Sul": "MS",
        "Mato Grosso": "MT",
        "Goiás": "GO",
        "Distrito Federal": "DF",
    }

    xl_ibge = pd.ExcelFile("C:\\Users\\danilo.araujo\\python\\python_estudos\\dados\\RELATORIO_DTB_BRASIL_MUNICIPIO.xls")
    df_ibge = xl_ibge.parse(sheet_name=0, header=6, usecols=["Nome_UF", "Nome_Município"])

    municipios_ibge_upper = [item.upper() for item in df_ibge["Nome_Município"]]
    municipios_ibge_tratados = [tratar_caracteres_especiais(item) for item in municipios_ibge_upper]

    df_ibge["UF_Sigla"] = df_ibge["Nome_UF"].replace(siglas_estados)
    df_ibge["municipios_ibge_upper"] = municipios_ibge_upper
    df_ibge["municipios_ibge_tratados"] = municipios_ibge_tratados

    xl_ibge.close()

    print(df_ibge)

    return df_ibge

def tratar_caracteres_especiais(palavra: str):
    # 1 - Isso aqui remove os acentos da palavra -> ç, á, à, ã, ä
    palavra_tratada = unidecode(palavra)

    # 2 - Aqui vamos remover os caracteres especiais -> ', `, ´
    caracteres_1 = "'´`"
    for i in range(0, len(caracteres_1)):
        # trocar caractere por "backspace"
        palavra_tratada = palavra_tratada.replace(caracteres_1[i], "")

    # 3 - Aqui vamos remover os caracteres especiais -> -, _,
    caracteres_2 = "-_"
    for i in range(0, len(caracteres_2)):
        # Trocar caractere por "espaço"
        palavra_tratada = palavra_tratada.replace(caracteres_2[i], " ")

    return palavra_tratada


def pesquisar_leven(municipio_pessoa: str, coluna: pd.Series):
    calibrador = 3
    municipios_ibge_upper = coluna
    lista_leven_aceitavel = []
    for municipio_ibge in municipios_ibge_upper:
        distancia_leven = jf.levenshtein_distance(municipio_pessoa, municipio_ibge)
        if distancia_leven > calibrador:
            continue
        else:
            lista_leven_aceitavel.append(municipio_ibge)
    print(lista_leven_aceitavel)

df_ibge = gerar_df_ibge()

pesquisar_leven("TRÊSCORAÇÕES", df_ibge["municipios_ibge_upper"])