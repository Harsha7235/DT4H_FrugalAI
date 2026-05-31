import copy
import numpy as np

def generate_future_clone(
    current_data,
    probability,
    heart,
    liver,
    pancreas,
    kidney,
    optimized_dose
):
    """
    Simulates:
    - 6 month progression without intervention
    - 6 month projection with intervention
    """

    # Clone current state
    baseline = {
        "probability": probability,
        "heart": heart,
        "liver": liver,
        "pancreas": pancreas,
        "kidney": kidney
    }

    # ---- Scenario 1: No Intervention (Natural Drift) ----
    drift_factor = 0.08  # 8% worsening over 6 months

    no_intervention = {
        "probability": min(1, probability * (1 + drift_factor)),
        "heart": min(100, heart * (1 + drift_factor)),
        "liver": min(100, liver * (1 + drift_factor)),
        "pancreas": min(100, pancreas * (1 + drift_factor)),
        "kidney": min(100, kidney * (1 + drift_factor)),
    }

    # ---- Scenario 2: With Intervention ----
    improvement_factor = 0.12  # 12% improvement

    with_intervention = {
        "probability": max(0, probability * (1 - improvement_factor)),
        "heart": max(0, heart * (1 - improvement_factor)),
        "liver": max(0, liver * (1 - improvement_factor)),
        "pancreas": max(0, pancreas * (1 - improvement_factor)),
        "kidney": max(0, kidney * (1 - improvement_factor)),
        "dose_used": optimized_dose
    }

    # ---- Delta Comparison ----
    delta = {
        "probability_change_no_intervention":
            round(no_intervention["probability"] - probability, 4),

        "probability_change_with_intervention":
            round(with_intervention["probability"] - probability, 4),

        "heart_delta":
            round(with_intervention["heart"] - heart, 2),

        "liver_delta":
            round(with_intervention["liver"] - liver, 2),

        "pancreas_delta":
            round(with_intervention["pancreas"] - pancreas, 2),

        "kidney_delta":
            round(with_intervention["kidney"] - kidney, 2)
    }

    return {
        "baseline": baseline,
        "six_month_no_intervention": no_intervention,
        "six_month_with_intervention": with_intervention,
        "delta_analysis": delta
    }