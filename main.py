from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



app = FastAPI()

# CORS 設定（フロントエンドからのリクエスト許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:3000", 
    "http://127.0.0.1:3000", 
    "https://ai-kondate-app2.vercel.app"
],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IngredientInput(BaseModel):
    ingredients: str

@app.get("/")
def read_root():
    return {"message": "AI献立アシスタントが起動中です🍳"}

