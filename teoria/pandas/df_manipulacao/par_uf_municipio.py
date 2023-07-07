import pandas as pd
#Solução de um colaborador no StackOverFlow

# Suponha que df seja o seu DataFrame
df = pd.DataFrame({
    'Nome_UF': ['RO', 'RO', 'RO', 'RO', 'RO', 'DF', 'DF'],
    'Código': [1100015, 1100379, 1100403, 1100346, 1100023, 1000, 2000],
    'Nome_Distrito': ['Alta Floresta D\'Oeste', 'Alto Alegre dos Parecis', 'Alto Paraíso', 'Alvorada D\'Oeste', 'Ariquemes', 'Brasília', 'Brasília']
})

print(df)

def check_uf_municipio(df, uf, distrito):
    # Verifica se a UF e o Município existem no DataFrame
    uf_exists = df['Nome_UF'].isin([uf])
    municipio_exists = df['Nome_Distrito'].isin([distrito])

    # Retorna um DataFrame onde ambos a UF e o Município existem
    result = df[uf_exists & municipio_exists]

    # Se o DataFrame resultante não estiver vazio, então o par UF/Município existe
    exists = not result.empty and len(result.index) == 1

    return exists

exists = check_uf_municipio(df, 'DF', 'Brasília')
print('Existe:', exists)

exists2 = check_uf_municipio(df, "RO", "Alto Paraíso")
print(exists2)