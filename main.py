from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os
from fastapi.middleware.cors import CORSMiddleware



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
    

origins = [
    "https://master.dvsj3evpic9gz.amplifyapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)