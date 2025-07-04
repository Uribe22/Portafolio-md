# main.py
from fastapi import FastAPI
from app.adapters.http.router import router

app = FastAPI()

app.include_router(router)
