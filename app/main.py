from fastapi import FastAPI
from pydantic import BaseModel
from app.core import normalize_latex

app = FastAPI()

# ✅ 루트 페이지 응답 추가 (브라우저 확인용)
@app.get("/")
def read_root():
    return {"message": "Welcome to math-api"}

class LatexInput(BaseModel):
    latex: str

@app.post("/normalize")
async def normalize_formula(data: LatexInput):
    hash_result = normalize_latex(data.latex)
    return {"hash": hash_result}
