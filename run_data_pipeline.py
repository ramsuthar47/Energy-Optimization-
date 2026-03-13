from src.data.load_data import load_energy_data
from src.data.preprocess import clean_data
from src.data.resample_data import convert_to_hourly
from src.data.save_processed import save_processed_data
from src.data.feature_engineering import create_features


RAW_PATH = "data/raw/household_power_consumption.txt"
OUTPUT_PATH = "data/processed/energy_hourly.csv"


def run_pipeline():

    print("Loading dataset...")
    df = load_energy_data(RAW_PATH, nrows=200000)

    print("Cleaning dataset...")
    df = clean_data(df)

    print("Converting to hourly data...")
    df_hourly = convert_to_hourly(df)

    print("Creating features...")
    df_features = create_features(df_hourly)

    print("Saving processed data...")
    save_processed_data(df_features, OUTPUT_PATH)

    print("Pipeline completed.")


if __name__ == "__main__":
    run_pipeline()