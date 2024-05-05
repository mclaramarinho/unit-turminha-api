from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from router.api import router

def startup_db_client():
    print(f"Connected")

def shutdown_db_client():
    print("Mongo db client closed")

@asynccontextmanager
async def lifespan(app: FastAPI):
    startup_db_client()
    yield
    app
    shutdown_db_client()


app = FastAPI(
    lifespan=lifespan
)


@app.get("/")
async def root() -> dict:
    return {"message": "MongoDB - Root"}


@app.get("/ping")
async def pong() -> str:
    return 'pong'


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
                   )

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)