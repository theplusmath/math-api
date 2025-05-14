from fastapi import APIRouter
from pydantic import BaseModel
from latex2sympy import latex2sympy, get_default_conf
import sympy
import re
import hashlib

router = APIRouter()

class LatexInput(BaseModel):
    latex: str

def normalize_latex(latex: str) -> str:
    # 간단한 정규화 예시: 알파벳을 VAR, 숫자를 NUM으로 대체
    latex = re.sub(r'[a-zA-Z]+', 'VAR', latex)
    latex = re.sub(r'[0-9]+', 'NUM', latex)
    return hashlib.sha1(latex.encode('utf-8')).hexdigest()

def parse_latex_tree(latex: str):
    try:
        expr = latex2sympy(latex, get_default_conf())
        return sympy.srepr(expr)
    except Exception as e:
        return {"error": str(e)}

def extract_keywords(tree_str: str):
    return list(set(re.findall(r"[A-Za-z_]+", tree_str)))

@router.post("/normalize")
async def normalize_formula(data: LatexInput):
    latex = data.latex
    hash_result = normalize_latex(latex)
    tree = parse_latex_tree(latex)
    keywords = extract_keywords(str(tree)) if isinstance(tree, str) else []

    return {
        "hash": hash_result,
        "tree": tree,
        "keywords": keywords
    }
