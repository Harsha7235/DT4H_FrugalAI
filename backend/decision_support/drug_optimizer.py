import numpy as np

def optimize_dose(current_dose, probability, organ_stress):

    # Safety factor
    safety_index = (probability + organ_stress/100) / 2

    if safety_index > 0.7:
        recommended_dose = current_dose * 0.6
        adjustment = "Reduce dose to prevent toxicity."
    elif safety_index > 0.4:
        recommended_dose = current_dose * 0.8
        adjustment = "Slight dose adjustment recommended."
    else:
        recommended_dose = current_dose
        adjustment = "Current dose within therapeutic window."

    therapeutic_window_low = recommended_dose * 0.8
    therapeutic_window_high = recommended_dose * 1.2

    return {
        "recommended_dose": round(recommended_dose,2),
        "adjustment_reason": adjustment,
        "therapeutic_window": [
            round(therapeutic_window_low,2),
            round(therapeutic_window_high,2)
        ]
    }