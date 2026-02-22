import pandas as pd
import numpy as np

np.random.seed(42)
n = 2000

data = pd.DataFrame({
    "age": np.random.randint(20, 80, n),
    "bmi": np.random.normal(25, 5, n),
    "bp": np.random.normal(120, 15, n),
    "glucose": np.random.normal(110, 30, n),
    "cholesterol": np.random.normal(200, 40, n),
    "sleep_hours": np.random.normal(7, 1.5, n)
})

data["risk_score"] = (
    0.03*data["age"] +
    0.05*data["bmi"] +
    0.04*data["bp"] +
    0.06*data["glucose"] +
    0.04*data["cholesterol"] -
    0.2*data["sleep_hours"]
)

threshold = data["risk_score"].median()
data["risk"] = (data["risk_score"] > threshold).astype(int)

data.drop("risk_score", axis=1, inplace=True)

data.to_csv("health_data.csv", index=False)

print("Dataset generated successfully")