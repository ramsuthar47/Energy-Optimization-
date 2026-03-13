from src.analytics.optimization_engine import generate_recommendations

DATA_PATH = "data/processed/energy_hourly.csv"

if __name__ == "__main__":

    generate_recommendations(DATA_PATH)