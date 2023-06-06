import pandas as pd
#Solução de um colaborador no StackOverFlow

# Suponha que df seja o seu DataFrame
df = pd.DataFrame({
    'Nome_UF': ['RO', 'RO', 'RO', 'RO', 'RO'],
    'Código Município Completo': [1100015, 1100379, 1100403, 1100346, 1100023],
    'Nome_Município': ['Alta Floresta D\'Oeste', 'Alto Alegre dos Parecis', 'Alto Paraíso', 'Alvorada D\'Oeste', 'Ariquemes']
})

def check_uf_municipio(df, uf, municipio):
    # Verifica se a UF e o Município existem no DataFrame
    uf_exists = df['Nome_UF'].isin([uf])
    municipio_exists = df['Nome_Município'].isin([municipio])

    # Retorna um DataFrame onde ambos a UF e o Município existem
    result = df[uf_exists & municipio_exists]

    # Se o DataFrame resultante não estiver vazio, então o par UF/Município existe
    exists = not result.empty

    return result, exists

# Testando a função
result, exists = check_uf_municipio(df, 'RO', 'Alta Floresta D\'Oeste')
print(result)
print('Existe:', exists)