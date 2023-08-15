import pandas as pd


def retorna_dados_mun_ibge(municipio: str, coluna: pd.Series, df: pd.DataFrame):
    mun_cod_ibge = df.loc[coluna == municipio, 'Código Município Completo'].item()
    mun_nome_ibge = df.loc[coluna == municipio, 'Nome_Município'].item()
    uf_cod_ibge = df.loc[coluna == municipio, 'UF'].item()
    uf_nome_ibge = df.loc[coluna == municipio, 'Nome_UF'].item()

    return mun_cod_ibge, mun_nome_ibge, uf_cod_ibge, uf_nome_ibge

