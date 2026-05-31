def organ_cascade(heart, liver, pancreas, kidney):

    # Cascading effect simulation
    liver += pancreas * 0.1
    heart += liver * 0.05
    kidney += liver * 0.08

    # Clamp values
    heart = min(100, heart)
    liver = min(100, liver)
    pancreas = min(100, pancreas)
    kidney = min(100, kidney)

    return heart, liver, pancreas, kidney