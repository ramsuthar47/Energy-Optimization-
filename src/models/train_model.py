import pandas as pd
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error


def train_model(data_path):

    print("Loading processed dataset...")

    df = pd.read_csv(data_path, parse_dates=["timestamp"])
    df = df.set_index("timestamp")

    y = df["Global_active_power"]

    X = df.drop(columns=["Global_active_power"])

    print("Splitting data...")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    print("Training XGBoost model...")

    model = xgb.XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )

    model.fit(X_train, y_train)

    print("Making predictions...")

    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds) ** 0.5

    print("Model Performance")
    print("MAE:", mae)
    print("RMSE:", rmse)

    return model