from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



app = FastAPI()
# CORS 設定（フロントエンドのドメインからのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-kondate-app.vercel.app",  # ←★ ここがとても重要！！
        "http://localhost:3000",              # ローカル環境
        "http://127.0.0.1:3000"               # ローカル環境
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

