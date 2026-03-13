def convert_to_hourly(df):

    df_hourly = df.resample("H").mean()

    return df_hourly