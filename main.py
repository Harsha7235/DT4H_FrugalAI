from fastapi import FastAPI
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("health_model.pkl")

@app.get("/")
def home():
    return {"message": "Digital Twin Healthcare API Running"}

@app.post("/predict")
def predict(data: dict):
    features = np.array([[
        data["age"],
        data["bmi"],
        data["bp"],
        data["glucose"],
        data["cholesterol"],
        data["sleep_hours"]
    ]])

    probability = model.predict_proba(features)[0][1]

    if probability > 0.75:
        decision = "High Risk – Consult Doctor"
    elif probability > 0.5:
        decision = "Moderate Risk – Improve Lifestyle"
    else:
        decision = "Low Risk – Healthy"

    return {
        "risk_probability": float(probability),
        "risk_level": decision
    }

@app.post("/simulate")
def simulate(data: dict):
    results = []
    glucose = data["glucose"]

    for day in range(10):
        glucose += np.random.normal(0, 2)
        features = np.array([[
            data["age"],
            data["bmi"],
            data["bp"],
            glucose,
            data["cholesterol"],
            data["sleep_hours"]
        ]])
        risk = model.predict_proba(features)[0][1]
        results.append(float(risk))

    return {"risk_over_time": results}

@app.post("/chat")
def chat(message: dict):
    text = message["text"].lower()

    if "reduce" in text:
        reply = "Increase sleep, reduce sugar intake, exercise daily."
    elif "glucose" in text:
        reply = "High glucose increases diabetes risk."
    elif "risk" in text:
        reply = "Risk is calculated using age, BMI, BP, glucose, cholesterol and sleep."
    else:
        reply = "Please ask health-related question."

    return {"reply": reply}