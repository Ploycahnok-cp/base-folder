from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRouter
import importlib
import os

app = FastAPI()

# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# dynamic routes
route_files = [file for file in os.listdir("app/routes") if file.endswith(".py")]
for file in route_files:
    module_name = f"app.routes.{file[:-3]}"
    module = importlib.import_module(module_name)

    if hasattr(module, "router") and isinstance(module.router, APIRouter):
        app.include_router(module.router)
