import pandas as pd

def existe_unico_municipio(df, coluna: pd.Series, municipio: str):

    ocorrencias = coluna.isin([municipio]) # retorna série em que todos os casos em que o argumento municipio aparece
    resultado = df[ocorrencias] # Gera um df com todas as ocorrencias do município no df original ('bonito', 4 linhas)
    numero_ocorrencias = len(resultado.index) # O número de ocorrencias é igual à quantidade de indices que aparecem no df
    print(numero_ocorrencias)
    if numero_ocorrencias == 1: # se for apenas uma, retorna true, do contrário retorna false
        return True
    else:
        return False

xl_ibge = pd.ExcelFile('dados/RELATORIO_DTB_BRASIL_DISTRITO_REDUZIDO.xls')
df_ibge = xl_ibge.parse(sheet_name=0, header=6, usecols=['Nome_UF', 'Nome_Município', 'Código Município Completo'])

# Perceba que esse relatório é um reduzido dos distritos, e não a lista completa dos municípios
print(existe_unico_municipio(df_ibge, df_ibge['Nome_Município'], 'Brasília'))