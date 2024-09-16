from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.configs import Settings

app = FastAPI()

# CORS
origins = [
    "http://localhost:5173",
    "https://main.dagez0h56fw8t.amplifyapp.com",
    "https://staging.dagez0h56fw8t.amplifyapp.com",
    "https://dev.dagez0h56fw8t.amplifyapp.com",
    "https://rmi.cpgcro.com",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/ping")
async def check_connection():
    return {"msg": "pong", "code": 200}
