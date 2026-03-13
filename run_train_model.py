from src.models.train_model import train_model

DATA_PATH = "data/processed/energy_hourly.csv"


if __name__ == "__main__":

    model = train_model(DATA_PATH)