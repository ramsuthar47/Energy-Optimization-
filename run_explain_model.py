from src.analytics.explain_model import explain_model

DATA_PATH = "data/processed/energy_hourly.csv"

if __name__ == "__main__":

    explain_model(DATA_PATH)