import pandas as pd


def create_features(df):

    df = df.copy()

    df["hour"] = df.index.hour
    df["day_of_week"] = df.index.dayofweek
    df["month"] = df.index.month

    df["lag_1"] = df["Global_active_power"].shift(1)
    df["lag_24"] = df["Global_active_power"].shift(24)

    df["rolling_mean_6"] = df["Global_active_power"].rolling(6).mean()
    df["rolling_mean_24"] = df["Global_active_power"].rolling(24).mean()

    df = df.dropna()

    return df