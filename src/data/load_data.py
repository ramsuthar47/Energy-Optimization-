import pandas as pd

def load_energy_data(filepath, nrows=None):

    df = pd.read_csv(
        filepath,
        sep=";",
        nrows=nrows,
        na_values=["?"],
        parse_dates={"timestamp": ["Date", "Time"]},
        infer_datetime_format=True,
        low_memory=False
    )

    df.set_index("timestamp", inplace=True)

    return df