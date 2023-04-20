from fastapi import FastAPI
from pydantic import BaseModel
from crime-analysis import crime_analysis

app = FastAPI()

class InputData(BaseModel):
    # Define your input schema here
    pass

@app.post("/predict")
async def predict(input: InputData):
    result = crime_analysis(input)
    return {"result": result}
