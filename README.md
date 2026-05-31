# Autonomous Healthcare Digital Twin System

## Mid-Semester CPS Project
**Amrita Vishwa Vidyapeetham, Coimbatore**

An Explainable AI (XAI) based Digital Twin platform for healthcare monitoring, disease prediction, risk analysis, organ stress visualization, drug simulation, and clinical decision support.

---

## Project Overview

This project creates a virtual digital representation (Digital Twin) of a patient using clinical biomarkers, medical history, disease conditions, and medication information.

The system analyzes patient health status using Machine Learning models and provides:

- Real-time health risk prediction
- Multi-disease prediction
- Organ stress visualization
- Drug PK/PD simulation
- Disease progression forecasting
- Monte Carlo uncertainty analysis
- SHAP Explainable AI
- Clinical recommendation engine
- MLOps monitoring dashboard
- EHR integration architecture

---

## Problem Statement

Traditional healthcare systems often identify diseases only after symptoms become severe.

A Digital Twin enables:

- Early risk detection
- Preventive healthcare
- Personalized treatment planning
- Drug response simulation
- Explainable AI assisted decision making

---

## Dataset

### Training Dataset

- 10,000 MIMIC-III inspired patient records
- Multi-disease healthcare dataset
- Synthetic but clinically realistic patient population

### Features Used

1. Age
2. BMI
3. Systolic Blood Pressure
4. Glucose
5. HbA1c
6. Creatinine
7. ALT
8. Troponin
9. eGFR
10. Cholesterol
11. Smoking Status
12. Drug Dosage Factor

---

## Machine Learning Architecture

### Random Forest Ensemble

The primary prediction engine uses:

- 15 Decision Trees
- Bootstrap Sampling
- Random Feature Selection
- Ensemble Voting
- Probability Averaging

Each tree focuses on different physiological systems:

- Cardiac
- Renal
- Metabolic
- Hepatic
- Lifestyle
- Multi-system interactions

### Prediction Pipeline

Patient Data
↓
Feature Extraction
↓
Random Forest
↓
Risk Probability
↓
SHAP Explainability
↓
Clinical Recommendations

---

## Explainable AI (SHAP)

The project uses SHAP-inspired explainability to identify:

- Which biomarkers increase risk
- Which biomarkers reduce risk
- Individual feature contribution
- Patient-specific explanations

Example:

Risk Score = 68%

Contributing Factors:

- Troponin +18%
- Blood Pressure +12%
- Cholesterol +8%
- Smoking +6%

Protective Factors:

- Good eGFR −5%
- Controlled HbA1c −3%

---

## Multi-Disease Prediction

Separate models estimate risk for:

### Heart Disease

Uses:

- Troponin
- Blood Pressure
- Cholesterol
- Smoking
- Age

### Diabetes

Uses:

- Glucose
- HbA1c
- BMI
- Age

### Chronic Kidney Disease

Uses:

- Creatinine
- eGFR
- Blood Pressure
- Glucose

---

## Organ Stress Modeling

Four organs are continuously monitored:

### Heart

Based on:

- Troponin
- Blood Pressure
- Cholesterol

### Kidney

Based on:

- Creatinine
- eGFR

### Liver

Based on:

- ALT
- Medication burden

### Pancreas

Based on:

- Glucose
- HbA1c

Stress values range:

- 0–30 : Low
- 31–55 : Moderate
- 56–75 : High
- 76–100 : Critical

---

## Disease Progression Simulation

Predicts future risk trajectory.

Formula:

Risk(t) = Probability × (1 + t/60)

Where:

- Risk(t) = Future Risk
- Probability = Current Risk
- t = Time

Outputs:

- 12 Month Forecast
- Organ Stress Trends
- Risk Evolution Curves

---

## Monte Carlo Simulation

Generates multiple future risk scenarios.

Purpose:

- Uncertainty Analysis
- Confidence Estimation
- Risk Distribution Modeling

Process:

1. Start with base risk.
2. Add controlled random variations.
3. Generate 200 simulations.
4. Calculate mean and standard deviation.
5. Estimate confidence score.

Outputs:

- Confidence
- Variance
- Distribution Histogram

---

## Drug PK/PD Simulation

### Pharmacokinetics (PK)

Studies:

- Drug absorption
- Drug distribution
- Drug elimination

Formula:

C(t) = (Dose + 1)e^(-t/12)

Where:

- C(t) = Drug Concentration
- Dose = Administered Drug
- t = Time

### Pharmacodynamics (PD)

Studies:

- Drug effect on organs
- Drug response
- Toxicity impact

---

## Clinical Recommendation Engine

Automatically generates recommendations based on:

- Blood Pressure
- Glucose
- HbA1c
- Creatinine
- eGFR
- Cholesterol
- Troponin
- Organ Stress

Priority Levels:

- Critical
- High
- Medium
- Low

---

## MLOps Pipeline

The project includes simulated MLOps monitoring.

Features:

- Experiment Tracking
- Model Registry
- Accuracy Monitoring
- AUC-ROC Tracking
- F1 Score Evaluation
- Drift Monitoring
- Staging Environment
- Production Environment

Models:

- Random Forest
- XGBoost
- Logistic Regression
- Neural Network

---

## EHR Integration

Healthcare interoperability architecture based on:

- HL7 FHIR
- Epic Integration
- Cerner Integration

Supports:

- Patient Records
- Lab Reports
- Prescriptions
- Clinical Notes

---

## Technology Stack

### Frontend

- React.js
- JavaScript
- Tailwind CSS

### Visualization

- Recharts
- Three.js

### AI / Analytics

- Random Forest
- XGBoost
- SHAP Explainability
- Monte Carlo Simulation

### Healthcare Standards

- HL7 FHIR
- EHR Architecture

---

## Key Features

✅ Real-Time Risk Dashboard

✅ Patient Deep Analysis

✅ Interactive Digital Twin

✅ Drug PK/PD Simulation

✅ SHAP Explainability

✅ Multi-Disease Prediction

✅ Clinical Recommendations

✅ Disease Progression Forecasting

✅ Monte Carlo Risk Analysis

✅ MLOps Dashboard

✅ EHR Integration

---

## Future Scope (Final Semester Version)

The final version will extend this project with:

- Real clinical datasets
- Wearable sensor integration
- Federated Learning
- Digital Twin synchronization
- Real-time hospital deployment
- Cloud-native MLOps
- Explainable Deep Learning
- Advanced Digital Twin Analytics
- Hospital-grade authentication and access control

---

# 🏥 Autonomous Digital Twin for Personalized Healthcare using Frugal AI and Intelligent Decision System

### CPS Semester Project | Amrita Vishwa Vidyapeetham

---

## 📌 Project Overview

This project presents an **Autonomous Digital Twin for Healthcare**, designed as a **Cyber Physical System (CPS)** that continuously monitors patient health parameters, creates a virtual patient model (Digital Twin), predicts health risks using Frugal AI, and provides intelligent healthcare recommendations.

The system integrates:

- MATLAB/Simulink based patient simulation
- Digital Twin Modeling
- Machine Learning based Risk Prediction
- Intelligent Decision Support System
- Real-Time Health Monitoring Framework
- Frugal AI for resource-efficient healthcare analytics

The primary objective is to demonstrate how Digital Twin Technology can transform healthcare from a reactive model into a predictive and personalized system.

---

## 🎯 Problem Statement

Traditional healthcare systems depend on periodic checkups and retrospective diagnosis.

This project aims to build a healthcare Cyber Physical System capable of:

- Continuous patient monitoring
- Real-time risk assessment
- Personalized healthcare recommendations
- Virtual patient simulation
- Intelligent decision support

using Digital Twin Technology and Frugal AI.

---

## 🏗 System Architecture

```text
Physical Patient
        │
        ▼
Sensor Inputs
(Heart Rate, BP, Glucose, BMI)
        │
        ▼
MATLAB / Simulink Model
        │
        ▼
Digital Twin Engine
        │
        ▼
Risk Prediction Module
        │
        ▼
Frugal AI Decision System
        │
        ▼
Healthcare Recommendations
        │
        ▼
Dashboard Visualization


⚙️ Simulink Implementation
The healthcare system is modeled using MATLAB/Simulink as a Cyber Physical System.
1. Physiological Data Generator
Simulates:
Heart Rate
Blood Pressure
Blood Glucose
Oxygen Saturation
Activity Levels
Outputs synthetic patient health data in real time.
2. Digital Twin Module
Creates a virtual representation of the patient.
Functions:
State Estimation
Health Synchronization
Patient Behavior Modeling
Continuous Updates
The digital twin continuously evolves according to incoming health parameters.
3. Risk Assessment Module
Predicts risks associated with:
Diabetes
Hypertension
Cardiovascular Diseases
Risk scores are generated dynamically using machine learning models.
4. Frugal AI Decision Engine
Provides:
Resource-efficient AI inference
Personalized healthcare recommendations
Risk mitigation strategies
Health optimization suggestions
Designed to minimize computational overhead while maintaining accuracy.
5. Feedback Controller
Implements a closed-loop healthcare monitoring mechanism.
Features:
Continuous monitoring
Adaptive recommendations
Dynamic risk updates
Personalized intervention planning


🤖 Frugal AI Component
The project incorporates Frugal AI principles:
Features
Lightweight Neural Networks
Reduced Computational Cost
Efficient Memory Usage
Fast Inference Time
Scalable Architecture
Benefits
Suitable for edge devices
Lower power consumption
Faster decision-making
Cost-effective deployment


📊 Simulation Outputs
The Simulink model generates:
Health Risk Curve
Displays disease risk progression over time.
Digital Twin Synchronization
Compares:
Physical Patient State
Virtual Patient State
Intervention Impact Analysis
Shows predicted outcomes after applying recommendations.
Health Stability Index
Measures patient wellness and overall health trend.


📈 Expected Results
Metric
Expected Value
Risk Prediction Accuracy
>90%
Twin Synchronization Accuracy
>95%
Decision Response Time
<1 second
Risk Detection Rate
>90%
Recommendation Accuracy
>85%


🔬 Research Contributions

This project contributes to healthcare research by:
Developing a Digital Twin based Healthcare CPS
Integrating Frugal AI into healthcare decision systems
Enabling real-time personalized healthcare monitoring
Creating an intelligent recommendation framework
Demonstrating predictive healthcare analytics


🛠 Technologies Used
MATLAB
Simulink
Stateflow
Control System Toolbox
Python
TensorFlow
Scikit-Learn
NumPy
Pandas
Frontend
React.js
Material UI
Plotly
Deployment
GitHub
Vercel


📂 Repository Structure
Plain text
DT4H_Project/

├── backend/
│   ├── main.py
│   ├── twin_engine.py
│   ├── risk_model.py
│   ├── decision_system.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── simulink/
│   ├── digital_twin_model.slx
│   ├── patient_generator.slx
│   └── risk_prediction.slx
│
├── data/
│   └── synthetic_dataset.csv
│
├── models/
│   └── risk_model.h5
│
├── results/
│   ├── accuracy_plot.png
│   ├── confusion_matrix.png
│   ├── risk_curve.png
│   └── simulation_output.png
│
├── docs/
│   ├── architecture.png
│   ├── system_design.png
│   └── screenshots/
│
└── README.md


🎓 Academic Relevance
Relevant Domains:
Cyber Physical Systems
Digital Twin Technology
Artificial Intelligence
Smart Healthcare
Intelligent Systems
Frugal AI
Personalized Medicine


🚀 Future Scope
Future enhancements include:
Wearable Device Integration
IoT Sensor Connectivity
Real-Time ECG Monitoring
Reinforcement Learning Based Intervention Planning
Explainable AI Dashboard
Federated Learning for Healthcare Privacy
Multi-Disease Prediction
Cloud-Based Digital Twin Deployment


📜 License
MIT License



👨‍💻 Author
Harsha
B.Tech Artificial Intelligence & Data Science
Specialization in Cyber Physical Systems and Security
Amrita Vishwa Vidyapeetham, Coimbatore
