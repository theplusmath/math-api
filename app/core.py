from sympy import latex, srepr
from sympy.parsing.latex import parse_latex
import hashlib
import re

# $~, $$~, \[ \], \(\), \displaystyle 등을 제거
def clean_latex_wrappers(latex_str):
    latex_str = re.sub(r"\$\$|\$|\\\[|\\\]|\\\(|\\\)|\\displaystyle", "", latex_str)
    return latex_str.strip()

def normalize_latex(latex_str):
    try:
        cleaned = clean_latex_wrappers(latex_str)
        expr = parse_latex(cleaned)

        hash_value = hashlib.sha256(latex_str.encode()).hexdigest()
        formula_tree = srepr(expr)
        keywords = list({type(atom).__name__ for atom in expr.atoms()})
        normalized_latex = latex(expr)
        sympy_expr = srepr(expr)

        return {
            "hash": hash_value,
            "main_formula_tree": formula_tree,
            "formula_keywords": keywords,
            "original_latex": latex_str,
            "normalized_latex": normalized_latex,
            "sympy_expr": sympy_expr
        }

    except Exception as e:
        return {"error": str(e)}
