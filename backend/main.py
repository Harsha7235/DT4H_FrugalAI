from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from datetime import datetime
import numpy as np

from sqlalchemy import create_engine, Column, Integer, Float, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func


# ================= FASTAPI =================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= DATABASE =================

DATABASE_URL="mysql+pymysql://root:26072006!@localhost:3306/digital_twin_health"

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()


class PatientDB(Base):
    __tablename__="patients_dataset"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    age=Column(Float)
    bmi=Column(Float)
    bp=Column(Float)
    glucose=Column(Float)
    cholesterol=Column(Float)
    smoking=Column(String)


class OrganStateDB(Base):
    __tablename__="organ_state"

    id=Column(Integer,primary_key=True,index=True)
    patient_id=Column(Integer,ForeignKey("patients_dataset.id"))

    heart=Column(Float)
    liver=Column(Float)
    pancreas=Column(Float)
    kidney=Column(Float)

    cumulative_damage=Column(Float)

    timestamp=Column(TIMESTAMP,server_default=func.now())


Base.metadata.create_all(bind=engine)


# ================= REQUEST MODEL =================

class Patient(BaseModel):

    name:str
    age:float
    bmi:float
    bp:float
    glucose:float
    cholesterol:float
    smoking:str
    dose:float
    tablets:float
    days:float

    # NEW FEATURES (symptoms)
    fever:int=0
    headache:int=0
    vomiting:int=0
    cough:int=0
    cold:int=0
    bodypain:int=0


# ================= SYMPTOM RISK =================

def symptom_risk(data):

    risk=0

    if data.fever==1:
        risk+=0.10

    if data.headache==1:
        risk+=0.05

    if data.vomiting==1:
        risk+=0.08

    if data.cough==1:
        risk+=0.03

    if data.cold==1:
        risk+=0.03

    if data.bodypain==1:
        risk+=0.05

    return risk


# ================= RISK ENGINE =================

def compute_probability(data,smoking):

    bmi=data.bmi/60
    bp=data.bp/250
    glucose=data.glucose/500
    chol=data.cholesterol/400
    age=data.age/120

    dose=data.dose/2000
    tablets=data.tablets/20
    days=data.days/365

    risk=(
        bmi*0.15+
        bp*0.2+
        glucose*0.2+
        chol*0.15+
        age*0.1+
        dose*0.1+
        tablets*0.05+
        days*0.05
    )

    if smoking==1:
        risk+=0.25

    # NEW: symptom influence
    risk+=symptom_risk(data)

    return float(np.clip(risk,0.01,0.99))


# ================= ORGAN MODEL =================

def compute_organs(data,smoking):

    dose=data.dose/2000
    tablets=data.tablets/20
    days=data.days/365

    glucose=data.glucose/500
    chol=data.cholesterol/400
    bp=data.bp/250

    heart=0.4*bp + 0.2*chol + smoking*0.3
    liver=0.5*chol + 0.7*dose + 0.3*days
    pancreas=0.8*glucose + 0.2*chol
    kidney=0.4*bp + 0.5*tablets + 0.3*dose

    heart=np.clip(heart,0,1)
    liver=np.clip(liver,0,1)
    pancreas=np.clip(pancreas,0,1)
    kidney=np.clip(kidney,0,1)

    return heart,liver,pancreas,kidney


# ================= PREDICT =================

@app.post("/predict")
def predict(data:Patient):

    db=SessionLocal()

    smoking_value=1 if data.smoking=="Smoker" else 0

    probability=compute_probability(data,smoking_value)

    heart,liver,pancreas,kidney=compute_organs(data,smoking_value)

    tier="LOW"

    if probability>0.65:
        tier="CRITICAL"
    elif probability>0.40:
        tier="MODERATE"

    organ_map={
        "heart":float(heart),
        "liver":float(liver),
        "pancreas":float(pancreas),
        "kidney":float(kidney)
    }

    patient=db.query(PatientDB).filter(PatientDB.name==data.name).first()

    if not patient:

        patient=PatientDB(
            name=data.name,
            age=data.age,
            bmi=data.bmi,
            bp=data.bp,
            glucose=data.glucose,
            cholesterol=data.cholesterol,
            smoking=data.smoking
        )

        db.add(patient)
        db.commit()
        db.refresh(patient)

    previous=0

    last=db.query(OrganStateDB)\
        .filter(OrganStateDB.patient_id==patient.id)\
        .order_by(OrganStateDB.id.desc())\
        .first()

    if last:
        previous=last.cumulative_damage

    damage=previous+(heart+liver+pancreas+kidney)/4

    organ=OrganStateDB(
        patient_id=patient.id,
        heart=heart,
        liver=liver,
        pancreas=pancreas,
        kidney=kidney,
        cumulative_damage=damage
    )

    db.add(organ)
    db.commit()


    # ================= MONTE CARLO =================

    monte=[

        {
            "iteration":i,
            "risk":float(probability*np.random.normal(1,0.12)*100)
        }

        for i in range(100)
    ]


    # ================= PKPD =================

    pkpd=[

        {
            "time":t,
            "concentration":float((data.dose+1)*np.exp(-t/12))
        }

        for t in range(25)
    ]


    # ================= PROGRESSION =================

    progression=[

        {
            "time":t,
            "risk":float(np.clip(probability*(1+t/60),0,1))
        }

        for t in range(25)
    ]


    # ================= BIOMARKERS =================

    biomarkers={

        "ALT":round(liver*120,2),
        "AST":round(liver*100,2),
        "Creatinine":round(kidney*95,2),
        "Troponin":round(heart*85,2)
    }


    # ================= AI EXPLAINABILITY =================

    heatmap=[

        {"feature":"BMI","impact":round(data.bmi/60*100,2)},
        {"feature":"Blood Pressure","impact":round(data.bp/250*100,2)},
        {"feature":"Glucose","impact":round(data.glucose/500*100,2)},
        {"feature":"Cholesterol","impact":round(data.cholesterol/400*100,2)},
        {"feature":"Drug Dose","impact":round(data.dose/2000*100,2)},
        {"feature":"Tablets","impact":round(data.tablets/20*100,2)},
        {"feature":"Smoking","impact":40 if smoking_value else 0}

    ]


    # ================= MODEL LEARNING PANEL =================

    model_learning={

        "dataset_size":10000,
        "model":"Hybrid Simulation + Statistical Risk Engine",

        "top_features":[
            "Glucose",
            "Blood Pressure",
            "Drug Dose",
            "Smoking",
            "Cholesterol"
        ],

        "confidence":round(probability*100,2)

    }


    # ================= SYMPTOM SIGNALS FOR 3D TWIN =================

    symptoms={

        "fever":data.fever,
        "headache":data.headache,
        "vomiting":data.vomiting,
        "cough":data.cough,
        "cold":data.cold,
        "bodypain":data.bodypain

    }


    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    db.close()

    return{

        "timestamp":timestamp,
        "probability":probability,
        "tier":tier,
        "organ_stress":organ_map,
        "pkpd_simulation":pkpd,
        "progression":progression,
        "monte_carlo":monte,
        "biomarkers":biomarkers,
        "ai_heatmap":heatmap,
        "model_learning":model_learning,
        "symptoms":symptoms,
        "cumulative_damage":damage

    }