import joblib
import os

class ModelLoader:

    def load_all(self):

        model_path = os.path.join("models", "digital_twin_model.pkl")
        scaler_path = os.path.join("models", "scaler.pkl")

        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)

        models = {
            "risk_model": model
        }

        return models, scaler