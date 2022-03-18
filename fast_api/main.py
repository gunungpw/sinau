from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World Earth"}


@app.get("/day")
async def root():
    today = datetime.today()
    return {"Today": f"{today}"}
