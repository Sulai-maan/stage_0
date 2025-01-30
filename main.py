from statics import data, ORIGINS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

@app.get("/")
async def root():
    return json.dumps(data)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_methods=["GET"]
)