import numpy as np

class Predictor:

    def __init__(self, models, scaler):

        self.model = models["risk_model"]
        self.scaler = scaler

    def predict_all(self, data):

        X = np.array([[
            data.age,
            data.bmi,
            data.bp,
            data.bp * 0.65,
            data.glucose,
            data.cholesterol,
            data.smoking,
            data.dose,
            data.tablets,
            data.days
        ]])

        X_scaled = self.scaler.transform(X)

        preds = self.model.predict(X_scaled)[0]

        heart = float(preds[0])
        liver = float(preds[1])
        pancreas = float(preds[2])
        kidney = float(preds[3])

        # convert to normalized risk
        heart = max(0, min(100, heart * 100))
        liver = max(0, min(100, liver * 100))
        pancreas = max(0, min(100, pancreas * 100))
        kidney = max(0, min(100, kidney * 100))

        probability = (heart + liver + pancreas + kidney) / 400

        return probability, heart, liver, pancreas, kidney