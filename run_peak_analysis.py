from src.analytics.peak_detection import detect_peak_hours

DATA_PATH = "data/processed/energy_hourly.csv"

if __name__ == "__main__":

    detect_peak_hours(DATA_PATH)