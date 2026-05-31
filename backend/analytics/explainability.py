import numpy as np

FEATURE_NAMES = [
    "Age",
    "BMI",
    "Blood Pressure",
    "Glucose",
    "Cholesterol",
    "Smoking",
    "Dose",
    "Tablets",
    "Days"
]

def explain_prediction(model, scaler, data):
    """
    Returns feature contribution ranking for toxicity prediction.
    Works with LogisticRegression model.
    """

    X = np.array([[data.age, data.bmi, data.bp,
                   data.glucose, data.cholesterol,
                   data.smoking, data.dose,
                   data.tablets, data.days]])

    # Scale input
    X_scaled = scaler.transform(X)

    # Get model coefficients
    coefficients = model.coef_[0]

    # Contribution = coef * feature value
    contributions = coefficients * X_scaled[0]

    explanation = []

    for i in range(len(FEATURE_NAMES)):
        explanation.append({
            "feature": FEATURE_NAMES[i],
            "impact_score": round(float(contributions[i]), 4)
        })

    # Sort by absolute impact
    explanation_sorted = sorted(
        explanation,
        key=lambda x: abs(x["impact_score"]),
        reverse=True
    )

    # Top 3 drivers
    top_drivers = explanation_sorted[:3]

    return {
        "all_features": explanation_sorted,
        "top_drivers": top_drivers
    }