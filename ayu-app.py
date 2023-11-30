"""
Nama : Ayu ....
Batch : ...
Objective : Memahami pembuatan REST API dengan FASTAPI 
"""

from fastapi import FastAPI, HTTPException
import pandas as pd



app = FastAPI()

@app.get("/")
def root():
  try : 
    df = pd.read_csv("data.csv")
    return df.to_dict(orient="records")
  except : 
    return HTTPException(status_code=500, detail="Internal server error")