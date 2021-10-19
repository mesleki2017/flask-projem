from fastapi import Request
from fastapi.staticfiles import StaticFiles
import json
import asyncio
from fastapi import FastAPI
from fastapi import Request
from fastapi import WebSocket
from fastapi.templating import Jinja2Templates
import uvicorn
from pathlib import Path
import numpy as np
import math
import time


start = time.time()

datam1={
    "x":0,
    "y":0
}

def sanal_data(data):
    
    frekans=10
    data["x"]=time.time() - start
    data["y"]=math.sin((2*math.pi*frekans)*data["x"])

   

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")




@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        sanal_data(datam1)
        await asyncio.sleep(0.00001)
        await websocket.send_json(datam1)


if __name__ == '__main__':
    uvicorn.run(app)