#main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post,user,auth,vote
from .config import settings
#models.Base.metadata.create_all(bind=engine)
#alembic handles it now

app = FastAPI()

origins = ["*"] #which websites can acces your api

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

my_posts = []

@app.get("/")
def root():
    return {"message": "welcome to my api!!!"}

app.include_router(post.router)
app.include_router(user.router) 
app.include_router(auth.router)
app.include_router(vote.router)

    