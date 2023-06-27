import pandas as pd
import csv
#
file_name = 'dados/RELATORIO_DTB_BRASIL_DISTRITO_REDUZIDO.xls'  # File name
sheet_name = 0
header = 6
#
# sheet = pd.read_excel(io = file_name, sheet_name = sheet_name, header = header)
# print(sheet.head()) # Prints first 5 rows from the top along with the header
# print(sheet.tail()) # Prints first 5 rows from the bottom along with the header

xl = pd.ExcelFile(file_name)
df = xl.parse(sheet_name, header=header, usecols=['Código Município Completo', 'Nome_Município'])
print(df)

df.to_csv(
    'exportar.csv', # Nome do arquivo
    mode='x', # Modo de escrita
    index=False, # Elimina a necessidade de escrever um 'id' para a 'tabela csv'
    na_rep='' # Nesse caso não será necessário, mas esse argumento fala pra escrever '' quando o campo for null
)
