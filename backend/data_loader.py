import mysql.connector
import pandas as pd

def load_patient_dataset():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="26072006!",
        database="digital_twin_health"
    )

    query = "SELECT * FROM patients_dataset"

    df = pd.read_sql(query, conn)

    conn.close()

    return df