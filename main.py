from fastapi import FastAPI
from app.routes.latex import router as latex_router

app = FastAPI(
    title="Math API",
    description="LaTeX 수식을 SymPy 형태로 변환해주는 API",
    version="0.1.0"
)

# /latex 경로로 라우터 연결
app.include_router(latex_router, prefix="/latex")
