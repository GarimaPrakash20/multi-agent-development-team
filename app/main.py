from fastapi import FastAPI
from app.routes import build_feature

app = FastAPI()

app.include_router(build_feature.router)
