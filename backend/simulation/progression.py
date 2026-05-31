import numpy as np

def simulate_progression(probability, heart, pancreas, kidney):

    years = np.linspace(0, 5, 60)  # 5 years monthly resolution

    # Base risk growth
    cv_risk = probability * np.exp(heart/200 * years)
    diabetes_risk = probability * np.exp(pancreas/180 * years)
    ckd_risk = probability * np.exp(kidney/170 * years)

    # Normalize to max 1
    cv_risk = np.clip(cv_risk, 0, 1)
    diabetes_risk = np.clip(diabetes_risk, 0, 1)
    ckd_risk = np.clip(ckd_risk, 0, 1)

    # Overall deterioration index
    deterioration = (cv_risk + diabetes_risk + ckd_risk) / 3

    return {
        "timeline_years": years.tolist(),
        "cv_risk_curve": cv_risk.tolist(),
        "diabetes_risk_curve": diabetes_risk.tolist(),
        "ckd_risk_curve": ckd_risk.tolist(),
        "deterioration_curve": deterioration.tolist(),
        "five_year_cv_probability": round(float(cv_risk[-1]),3),
        "five_year_diabetes_probability": round(float(diabetes_risk[-1]),3),
        "five_year_ckd_probability": round(float(ckd_risk[-1]),3)
    }