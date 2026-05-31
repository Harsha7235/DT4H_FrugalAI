import numpy as np

def accumulate_damage(previous_damage,
                      heart,
                      liver,
                      pancreas,
                      kidney,
                      age,
                      dose):

    # Weighted organ contribution
    organ_load = (
        0.3 * heart +
        0.3 * liver +
        0.2 * pancreas +
        0.2 * kidney
    )

    # Drug amplification factor
    drug_factor = 1 + (dose / 500)

    # Age-based resilience decay
    resilience = max(0.85 - (age / 200), 0.5)

    # Accumulation equation
    new_damage = (
        previous_damage * resilience +
        organ_load * drug_factor * 0.05
    )

    # Clamp to 0–100
    return round(min(max(new_damage, 0), 100), 2)