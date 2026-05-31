import shap
import numpy as np

class ShapExplainer:

    def __init__(self, model):
        self.model = model
        self.explainer = shap.TreeExplainer(model)

    def explain(self, scaler, data):

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

        X_scaled = scaler.transform(X)

        shap_values = self.explainer.shap_values(X_scaled)

        # If multi-output model
        if isinstance(shap_values, list):
            shap_values = shap_values[0]

        shap_values = np.array(shap_values).flatten()

        features = [
            "age",
            "bmi",
            "bp",
            "diastolic_bp",
            "glucose",
            "cholesterol",
            "smoking",
            "dose",
            "tablets",
            "days"
        ]

        explanation = []

        for i in range(len(features)):

            impact = float(shap_values[i])

            explanation.append({
                "feature": features[i],
                "impact": impact
            })

        return explanation