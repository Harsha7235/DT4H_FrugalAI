import numpy as np

def compute_drift(history_probs):

    if len(history_probs) < 5:
        return 0

    baseline = np.mean(history_probs[:3])
    recent = np.mean(history_probs[-3:])

    drift_score = abs(recent - baseline)

    return round(drift_score, 4)