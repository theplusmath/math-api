from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from latex2sympy import latex2sympy, get_default_conf
import sympy
import re
import hashlib

router = APIRouter()

# ✅ 수정: 여러 수식을 받는 모델
class LatexListInput(BaseModel):
    latex_list: List[str]

# 해시 생성 (정규화 기반)
def normalize_latex(latex: str) -> str:
    latex = re.sub(r'[a-zA-Z]+', 'VAR', latex)
    latex = re.sub(r'[0-9]+', 'NUM', latex)
    return hashlib.sha1(latex.encode('utf-8')).hexdigest()

# 트리 파싱
def parse_latex_tree(latex: str):
    try:
        expr = latex2sympy(latex, get_default_conf())
        return sympy.srepr(expr)
    except Exception as e:
        return {"error": str(e)}

# 키워드 추출
def extract_keywords(tree_str: str):
    return list(set(re.findall(r"[A-Za-z_]+", tree_str)))

# ✅ POST: 여러 수식 처리
@router.post("/normalize")
async def normalize_formula(data: LatexListInput):
    results = []
    for latex in data.latex_list:
        hash_result = normalize_latex(latex)
        tree = parse_latex_tree(latex)
        keywords = extract_keywords(str(tree)) if isinstance(tree, str) else []

        results.append({
            "latex": latex,
            "hash": hash_result,
            "tree": tree,
            "keywords": keywords
        })

    return results
