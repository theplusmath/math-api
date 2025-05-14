from fastapi import APIRouter
from pydantic import BaseModel
from latex2sympy import latex2sympy, get_default_conf

router = APIRouter()

class LatexInput(BaseModel):
    latex: str

@router.post("/parse")
async def parse_latex_api(data: LatexInput):
    try:
        conf = get_default_conf()
        expr = latex2sympy(data.latex, conf)
        return {
            "result": str(expr),
            "structure": str(type(expr))
        }
    except Exception as e:
        return {"error": str(e)}
