import pandas as pd 

def generate_recommendations(data_path):

    print("Loading dataset..")

    df = pd.read_csv(data_path, parse_dates=["timestamp"])
    df = df.set_index("timestamp")

    df["hour"] = df.index.hour

    hourly_usage = df.groupby("hour")["Global_active_power"].mean()

    peak_hour =  hourly_usage.idxmax()
    peak_value = hourly_usage.max()

    print("\nEnergy Optimization Recommendations")
    print("-----------------")

    print(f"Peak energy usage occurs at {peak_hour}:00")
    print(f"Average consumption at this time: {round(peak_value,2)} kW")

    off_peak_hour = hourly_usage.idxmax()
    off_peak_value = hourly_usage.min()

    print("\nSuggested Optimization:")

    print(f"Run high-energy appliances {off_peak_hour}:00 instead of {peak_hour}:00")

    estimated_saving = ((peak_value - hourly_usage.min()) / peak_value) * 100

    print(f"Estimated energy saving: {round(estimated_saving,1)}%")