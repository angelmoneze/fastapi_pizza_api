import imp
import fastapi as _fastapi
from pizza import pizza_router

app = _fastapi.FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {

        "message": "Hello World" 
    }

#importons les routes definies par pizza_router dans pizza
app.include_router(pizza_router)