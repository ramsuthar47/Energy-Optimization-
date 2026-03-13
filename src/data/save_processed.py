import pandas as pd

def save_processed_data(df, path):
    df.to_csv(path)

    print("Processed dataset saved to:", path)