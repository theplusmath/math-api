from fastapi import FastAPI
from pydantic import BaseModel
from app.core import normalize_latex

app = FastAPI()

class LatexInput(BaseModel):
    latex: str

@app.post("/normalize")
async def normalize_formula(data: LatexInput):
    hash_result = normalize_latex(data.latex)
    return {"hash": hash_result}
