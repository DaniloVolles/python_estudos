import pandas as pd
import numpy as np

excel_file = 'RELATORIO_DTB_BRASIL_DISTRITO_REDUZIDO.xls'
sheet = 0
header = 6

xl = pd.ExcelFile(excel_file)
df = xl.parse(sheet, header=header, usecols=['Código Município Completo', 'Nome_Município'])

# print(df.head()) # retorna o cabecalho do arquivo e os 5 primeiros itens
# print(df.columns) # retorna o cabecalho do arquivo
# print(df.index) # retorna quantas linhas a tabela possui.

print(df['Nome_Município'].unique()) # retorna qual o "range" de possibilidades de uma coluna -> 0 e 1, Masc e Fem etc.
# Repare que entre colchetes você seleciona a única coluna que você quer
print(df['Nome_Município'].value_counts()) # retorna as quantidades de cada item do range

