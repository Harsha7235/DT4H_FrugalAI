def stratify(probability):

    if probability < 0.25:
        tier = "Stable"
        color = "green"
    elif probability < 0.6:
        tier = "Moderate"
        color = "yellow"
    else:
        tier = "Critical"
        color = "red"

    confidence_interval = round(probability * 0.05, 3)

    return tier, color, confidence_interval