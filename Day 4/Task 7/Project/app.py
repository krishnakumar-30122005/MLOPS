import numpy as np
from fastapi import FastAPI
import joblib
from pydantic import BaseModel

model = joblib.load("Simple_model")

app = FastAPI()

class InputData(BaseModel):
    feature1: float


@app.post("/predict")
def predict(data:InputData):
    
    features = np.array([
        [data.feature1]
    ])

    prediction = model.predict(features)

    return {
        "prediction" : prediction.tolist()[0] 
    }
