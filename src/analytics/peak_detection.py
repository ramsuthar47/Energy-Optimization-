import pandas as pd

def detect_peak_hours(data_path):

    print("Loading processed dataset..")

    df = pd.read_csv(data_path, parse_dates=["timestamp"])
    df = df.set_index("timestamp")

    df["hour"] = df.index.hour

    hourly_usage = df.groupby("hour")["Global_active_power"].mean()

    peak_hour = hourly_usage.idxmax()
    peak_value = hourly_usage.max()

    print("\nPeak Usage Analysis")
    print("--------------")
    print("Peak Hour: ", peak_hour)
    print("Average Consumption: ", round(peak_value, 3))

    return hourly_usage