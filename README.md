# Stress Detection API 

Hi! This is my machine learning project where I built an API that can predict how stressed someone might be based on their daily habits like sleep, exercise, and heart rate. I'm still learning ML and web development, so this was a great practice project!

## What does this do?

Basically, you send some data about a person (like how much they sleep, their age, heart rate, etc.) and my API will predict their stress level on a scale. I trained a machine learning model using Python and then wrapped it in a web API so other apps can use it.

**Live Demo**: [My deployed UI](https://stress-detection-ui.vercel.app/) 

**Live API**: [My deployed API](https://stressdetection-model-api.onrender.com/) 

**Collab Notebook**: [Model Training](https://colab.research.google.com/drive/1zFovumnH23jQmn-bw1zwwL3NzLetxIu2?usp=sharing) 

## How I built this

I'm learning machine learning in college and wanted to try building something real. Here's what I used:

- **FastAPI** - for making the web API (way easier than Flask!)
- **scikit-learn** - for the machine learning model  
- **pandas** - for handling the data
- **Random Forest** - the ML algorithm I chose (seemed to work best in my tests)

## What you can do with it

### 1. Get a stress prediction
Send a POST request to `/predict` with this kind of data:

```json
{
    "sleep_duration": 7.5,
    "quality_of_sleep": 8,
    "age": 25,
    "heart_rate": 70,
    "daily_steps": 10000,
    "physical_activity_level": 7
}
```

And you'll get back something like:
```json
{
    "stress_level": 2,
    "status": "success"
}
```

### 2. Check how good my model is
Go to `/metrics` to see the accuracy and other stats about my model. Right now I'm getting around 85% accuracy which isn't bad for my first try!

## Running it yourself

If you want to try running this on your computer:

1. **Clone my repo**
```bash
git clone https://github.com/aaliawadkar1211/stressdetection-model-api.git
cd stressdetection-model-api
```

2. **Install the stuff you need**
```bash
pip install -r requirements.txt
```

3. **Start the API**
```bash
uvicorn main:app --reload
```

Then go to `http://localhost:8000/docs` to see the interactive documentation (FastAPI makes this automatically which is so cool!).

## The data it expects

Here's what each thing means:

- **sleep_duration**: How many hours you sleep (like 6.5, 8.0, etc.)
- **quality_of_sleep**: How good your sleep is, 1-10 scale
- **age**: Your age in years
- **heart_rate**: Your resting heart rate (beats per minute)
- **daily_steps**: How many steps you walk per day on average
- **physical_activity_level**: How active you are, 1-10 scale

## My project structure

```
my-stress-api/
├── main.py              # The main FastAPI app
├── model.pkl            # My trained model (saved with pickle)
├── requirements.txt     # All the Python packages I need
└── README.md           # This file!
```

## Things I learned

- How to train a machine learning model and save it
- FastAPI is really beginner-friendly compared to other frameworks
- Deploying ML models is harder than I thought!

## Known issues (still fixing these!)

- Sometimes the API returns weird results - still debugging the model
- Need to add better error handling
- Want to try other ML algorithms to improve accuracy
- The model file is pretty big, looking into ways to make it smaller



## Important note!

This is just a student project for learning! Don't actually use this to make decisions about your health. I'm not a doctor and this is just me practicing ML and web dev.

Built by me during my semester project 📚

---
*P.S. - This was way harder than I expected but super fun to build!*


