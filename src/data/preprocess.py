import pandas as pd

def clean_data(df):

    df = df.copy()

    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.fillna(method="ffill")

    return df