"""
Nama : 
Batch : 
Objective : Memahami pembuatan REST API dengan FASTAPI 
"""
import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
  try : 
    df = pd.read_csv('data.csv')
    return df.to_dict(orient='records')
  except : 
    return HTTPException(status_code=500, detail="Internal server error")

# pip install fastapi

# uvicorn filename:app --reload