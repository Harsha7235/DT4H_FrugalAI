import mysql.connector
import numpy as np
import random

conn = mysql.connector.connect(
host="localhost",
user="root",
password="26072006!",
database="digital_twin_health"
)

cursor = conn.cursor()

for i in range(10000):

    age = random.randint(20,85)

    gender = random.choice(["Male","Female"])

    bmi = round(np.random.normal(26,4),2)

    systolic_bp = round(np.random.normal(130,20),2)
    diastolic_bp = round(np.random.normal(85,10),2)

    glucose = round(np.random.normal(120,40),2)
    cholesterol = round(np.random.normal(200,35),2)

    smoking = random.randint(0,1)
    alcohol = random.randint(0,1)

    creatinine = round(np.random.normal(1.1,0.3),2)
    troponin = round(np.random.normal(0.04,0.02),3)

    alt = round(np.random.normal(40,10),2)
    ast = round(np.random.normal(35,10),2)

    dose = random.randint(100,800)
    tablets = random.randint(1,3)
    treatment_days = random.randint(10,90)

    cursor.execute("""

    INSERT INTO patients_dataset
    (age,gender,bmi,systolic_bp,diastolic_bp,
    glucose,cholesterol,smoking,alcohol,
    creatinine,troponin,alt,ast,
    dose,tablets,treatment_days)

    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

    """,(

    age,gender,bmi,
    systolic_bp,diastolic_bp,
    glucose,cholesterol,
    smoking,alcohol,
    creatinine,troponin,
    alt,ast,
    dose,tablets,treatment_days

    ))

conn.commit()

print("10000 patient records inserted")

cursor.close()
conn.close()