import numpy as np
from math import log

def simulate_pkpd(dose, age, days):

    # Basic pharmacokinetic assumptions
    Vd = 50  # distribution volume
    half_life = 8 + (age * 0.05)  # age-adjusted
    k = log(2) / half_life

    time = np.linspace(0, 24, 100)
    concentration = (dose / Vd) * np.exp(-k * time)

    peak = float(max(concentration))
    auc = float(np.trapz(concentration, time))

    return {
        "time_curve": time.tolist(),
        "concentration_curve": concentration.tolist(),
        "peak_concentration": round(peak, 3),
        "area_under_curve": round(auc, 3),
        "half_life": round(half_life, 2)
    }