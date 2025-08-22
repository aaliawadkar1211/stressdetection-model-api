# Stress Detection Model API

A simple **Stress Detection** API using machine learning!  
It predicts a person’s stress level based on lifestyle and health data like sleep, heart rate, activity, and age. Built beginner-friendly using FastAPI, so you can run it, call it, and integrate it with a frontend app.

---

## 🚀 Features
- **Live prediction endpoint** (`/predict`) that accepts:
  - Sleep Duration
  - Quality of Sleep
  - Age  
  - Heart Rate  
  - Daily Steps  
  - Physical Activity Level  
- Outputs a **stress level** (integer scale).
- Exposes **metrics endpoint** (`/metrics`) for viewing model performance (accuracy, precision, recall, confusion matrix).
- Built using a **Random Forest** model trained via scikit-learn.

---

## 🛠️ Tech Stack
- **Backend API**: FastAPI + Uvicorn  
- **ML & Serialization**: scikit-learn, pandas, pickle  
- **Deployment**: Ready to deploy to Render or similar services  
- **Frontend (optional demo)**: React / Next.js + Axios or Fetch API  

---
