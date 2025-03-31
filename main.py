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

@app.post("/recipe")
async def get_recipe(input: IngredientInput):
    prompt = f"{input.ingredients} を使った簡単な料理を1つ教えて。調理時間と足りない材料も教えて。"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return {"recipe": response.choices[0].message.content}
