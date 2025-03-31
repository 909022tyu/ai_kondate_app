from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()

# OpenAIクライアントを初期化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# FastAPIアプリの作成
app = FastAPI()

# CORS設定（フロントエンドのドメインを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-kondate-app2.vercel.app",  # ←ここが今使っているVercelのURL
        "https://ai-kondate-app.vercel.app",   # ←旧URL（必要なら残す）
        "http://localhost:3000",               # ←ローカル環境
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 入力データの型
class IngredientInput(BaseModel):
    ingredients: str

# 動作確認用のルートエンドポイント
@app.get("/")
def read_root():
    return {"message": "AI献立アシスタントが起動中です🍳"}

# レシピ生成エンドポイント
@app.post("/recipe")
async def get_recipe(input: IngredientInput):
    prompt = f"{input.ingredients} を使った簡単な料理を1つ教えて。調理時間と足りない材料も教えて。"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return {"recipe": response.choices[0].message.content}

