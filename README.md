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

## Author

Pittu.Harsha Vardhan Reddy

B.Tech Artificial Intelligence and Data Science
Specialization: Cyber Physical Systems and Security

Amrita Vishwa Vidyapeetham, Coimbatore

CPS Digital Twin Project – 2026
