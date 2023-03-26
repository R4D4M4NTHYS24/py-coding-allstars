from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os




SECRET = os.getenv("SECRET")

#
app = FastAPI()

@app.get("/bitcoin")
async def get_bitcoin_price():
    bitcoin_price = 60589.12 # Este es solo un ejemplo, debes implementar la lógica para obtener el precio actual
    return {"price": bitcoin_price}

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
    


