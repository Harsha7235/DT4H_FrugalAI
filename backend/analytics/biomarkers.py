def compute_biomarkers(probability, heart, liver, pancreas, kidney, data):

    metabolic_burden = (data.bmi * 0.3 + data.glucose * 0.4 + data.cholesterol * 0.3) / 10
    drug_load = (data.dose * data.tablets * data.days) / 5000
    aging_index = data.age * 0.2 + metabolic_burden * 0.3
    cardiometabolic_index = (heart + pancreas + metabolic_burden) / 3

    return {
        "metabolic_burden": round(metabolic_burden, 2),
        "drug_load_index": round(drug_load, 2),
        "aging_acceleration": round(aging_index, 2),
        "cardiometabolic_index": round(cardiometabolic_index, 2)
    }