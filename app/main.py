from fastapi import FastAPI
import numpy as np
from app import model
from app.schemas import StressRequest, StressResponse

app = FastAPI(title="Sleep & Stress Prediction API")

@app.get("/")
def home():
    return {"message": "Welcome to Sleep & Stress Prediction API 🚀"}

@app.post("/predict", response_model=StressResponse)
def predict(data: StressRequest):
    # Convert input to correct order
    input_data = np.array([[
        data.Sleep_Duration,
        data.Quality_of_Sleep,
        data.Age,
        data.Heart_Rate,
        data.Daily_Steps,
        data.Physical_Activity_Level
    ]])

    # Scale input
    input_scaled = model.scaler.transform(input_data)

    # Predict
    prediction = model.model.predict(input_scaled)[0]

    return StressResponse(stress_level=int(prediction))
