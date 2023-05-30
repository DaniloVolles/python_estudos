import pandas as pd

file_name = 'RELATORIO_DTB_BRASIL_DISTRITO.xls' # File name
sheet_name = 0
header = 6

sheet = pd.read_excel(io = file_name, sheet_name = sheet_name, header = header)
print(sheet.head()) # Prints first 5 rows from the top along with the header
print(sheet.tail()) # Prints first 5 rows from the bottom along with the header