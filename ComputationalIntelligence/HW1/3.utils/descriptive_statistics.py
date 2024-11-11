import pandas as pd

def calcular_estatisticas(df, coluna):
    """
    Calcula a média, mediana e desvio padrão de uma coluna numérica de um DataFrame.

    Parameters:
    df (pd.DataFrame): O DataFrame contendo os dados.
    coluna (str): O nome da coluna para calcular as estatísticas.

    Returns:
    dict: Um dicionário contendo média, mediana e desvio padrão, ou uma mensagem de erro se a coluna não for numérica.
    """
    if coluna not in df.columns:
        return {"erro": "A coluna especificada não existe no DataFrame."}

    if not pd.api.types.is_numeric_dtype(df[coluna]):
        return {"erro": "A coluna especificada não é numérica."}

    media = df[coluna].mean()
    mediana = df[coluna].median()
    desvio = df[coluna].std()

    return {
        "média": media,
        "mediana": mediana,
        "desvio padrão": desvio
    }
