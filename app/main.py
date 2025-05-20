from fastapi import FastAPI
from pydantic import BaseModel
from app.core import normalize_latex

app = FastAPI()

# ✅ 브라우저 테스트용 루트 페이지
@app.get("/")
def read_root():
    return {"message": "Welcome to math-api"}

# ✅ 입력 데이터 모델
class LatexInput(BaseModel):
    latex: str

# ✅ 수식 분석 API 엔드포인트
@app.post("/normalize")
async def normalize_formula(data: LatexInput):
    result = normalize_latex(data.latex)
    return result
