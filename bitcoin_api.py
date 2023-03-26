from fastapi import FastAPI

app = FastAPI()

@app.get("/bitcoin")
async def get_bitcoin_price():
    bitcoin_price = 60589.12 
    return {"price": bitcoin_price}
