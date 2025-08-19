from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained model
model = joblib.load("stress_model.joblib")

label_map = {
    0: "Low Stress",
    1: "Medium Stress",
    2: "High Stress"
}

class StressInput(BaseModel):
    hr_mean: float
    hr_std: float
    eda_mean: float
    eda_std: float
    temp_mean: float
    temp_std: float

app = FastAPI(title="Stress Detection API")

@app.get("/")
def root():
    return {"message": "Welcome to Stress Detection API 🚀"}

@app.post("/predict")
def predict(data: StressInput):
    df = pd.DataFrame([data.dict()])
    pred = model.predict(df)[0]
    return {
        "prediction": int(pred),
        "label": label_map.get(int(pred), "Unknown")
    }
