import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

from data_loader import load_patient_dataset


df = load_patient_dataset()


# FEATURES
X = df[[
"age",
"bmi",
"systolic_bp",
"diastolic_bp",
"glucose",
"cholesterol",
"smoking",
"dose",
"tablets",
"treatment_days"
]]


# TARGET ORGAN RISKS
y_heart = (
    df["systolic_bp"]/200 +
    df["cholesterol"]/300 +
    df["smoking"]*0.3
)

y_liver = (
    df["alt"]/120 +
    df["dose"]/800
)

y_pancreas = df["glucose"]/300

y_kidney = (
    df["creatinine"]/2 +
    df["age"]/100
)


# SPLIT
X_train,X_test,y_train,y_test = train_test_split(
    X,
    np.column_stack([y_heart,y_liver,y_pancreas,y_kidney]),
    test_size=0.2,
    random_state=42
)


# SCALE
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# MODEL
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train,y_train)


print("Training score:",model.score(X_test,y_test))


# SAVE MODELS
joblib.dump(model,"models/digital_twin_model.pkl")
joblib.dump(scaler,"models/scaler.pkl")

print("Models saved.")