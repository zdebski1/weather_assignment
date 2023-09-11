from fastapi import FastAPI
import requests
import weather_api
import httpx



app = FastAPI()

app.include_router(weather_api.router)

# python -m uvicorn diagram:app --reload
