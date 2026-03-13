import pandas as pd 
import shap 
import xgboost as xgb

def explain_model(data_path):

    print("Loading dataset..")

    df = pd.read_csv(data_path, parse_dates=["timestamp"])
    df = df.set_index("timestamp")

    y = df["Global_active_power"]
    X = df.drop(columns=["Global_active_power"])

    print("Training model for SHAP analysis...")

    model = xgb.XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )

    model.fit(X, y)

    print("Computing SHAP values..")

    explainer = shap.Explainer(model)
    shap_values = explainer(X)

    print("\nFeature Importance (Average Impact):")

    importance = pd.DataFrame({
        "feature": X.columns,
        "importance": abs(shap_values.values).mean(axis=0)
    })

    importance = importance.sort_values("importance", ascending=False)

    print(importance.head(10))

    return(importance)