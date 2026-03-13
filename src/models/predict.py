import joblib

def load_model(path="models/energy_model.pkl"):
    return joblib.load(path)

def predict_energy(model, features):
    return model.predict(features)