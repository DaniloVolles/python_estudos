import pandas as pd

excel_file = 'dados/RELATORIO_DTB_BRASIL_DISTRITO_REDUZIDO.xls'
sheet = 0
header = 6
xl = pd.ExcelFile(excel_file)
df = xl.parse(sheet, header=header, usecols=['Nome_UF', 'Nome_Município'])

# uf = df['Nome_UF'].isin(['Amapá']) # Retorna uma série de booleanos

uf = df.loc[df['Nome_UF'] == 'Amapá']

print(uf)