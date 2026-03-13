import joblib

def save_model(model, path="models/energy_model.pkl"):
    joblib.dump(model, path)