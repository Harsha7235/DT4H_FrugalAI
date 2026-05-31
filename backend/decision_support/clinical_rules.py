def generate_clinical_recommendations(tier, heart, liver, pancreas, kidney):

    recommendations = []
    monitoring = []
    urgency = "Routine"

    if tier == "Critical":
        urgency = "Immediate Medical Attention Required"
    elif tier == "Moderate":
        urgency = "Close Monitoring Required"

    # Organ-specific logic

    if pancreas > 60:
        recommendations.append("HbA1c test and fasting glucose monitoring recommended.")
        monitoring.append("Quarterly glycemic panel.")

    if heart > 60:
        recommendations.append("ECG and lipid profile assessment recommended.")
        monitoring.append("Cardiovascular risk reassessment in 3 months.")

    if liver > 60:
        recommendations.append("Liver Function Test (ALT, AST) required.")
        monitoring.append("Monitor hepatic enzymes monthly if on statins.")

    if kidney > 60:
        recommendations.append("eGFR and creatinine clearance evaluation recommended.")
        monitoring.append("Renal function monitoring every 2–3 months.")

    if not recommendations:
        recommendations.append("Maintain preventive health screening annually.")

    lifestyle = [
        "Maintain BMI below 25.",
        "Reduce processed sugar intake.",
        "Engage in 150 minutes of weekly aerobic exercise.",
        "Ensure adequate hydration and sleep cycle."
    ]

    return {
        "urgency": urgency,
        "recommendations": recommendations,
        "monitoring_plan": monitoring,
        "lifestyle_advice": lifestyle
    }