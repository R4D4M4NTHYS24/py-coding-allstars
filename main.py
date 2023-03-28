from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os






SECRET = os.getenv("SECRET")

#
app = FastAPI()

def get_currency_data():
    data = {
        "USD": 4658,
        "EUR": 5048,
        "JPY": 677,
       
    }
    top_currencies = dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:3])
    return top_currencies

@app.get("/currencies")
async def currencies():
    return get_currency_data()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    driver=createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    


