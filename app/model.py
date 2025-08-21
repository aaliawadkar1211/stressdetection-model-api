import pickle
import os

# Paths
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

# Load model
with open(os.path.join(MODEL_DIR, "stress_model.pkl"), "rb") as f:
    model = pickle.load(f)

# Load scaler
with open(os.path.join(MODEL_DIR, "scaler.pkl"), "rb") as f:
    scaler = pickle.load(f)

# Load features
with open(os.path.join(MODEL_DIR, "features.pkl"), "rb") as f:
    features = pickle.load(f)
