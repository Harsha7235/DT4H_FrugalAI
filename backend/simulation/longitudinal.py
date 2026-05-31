import random

def simulate_drift(heart, liver, pancreas, kidney):

    heart += random.uniform(-1, 1)
    liver += random.uniform(-1, 1)
    pancreas += random.uniform(-1, 1)
    kidney += random.uniform(-1, 1)

    heart = max(0, min(100, heart))
    liver = max(0, min(100, liver))
    pancreas = max(0, min(100, pancreas))
    kidney = max(0, min(100, kidney))

    return heart, liver, pancreas, kidney