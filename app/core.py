from sympy import sympify, latex, srepr
import hashlib

def normalize_latex(latex_str):
    try:
        expr = sympify(latex_str)

        hash_value = hashlib.sha256(latex_str.encode()).hexdigest()
        formula_tree = srepr(expr)
        keywords = list({type(atom).__name__ for atom in expr.atoms()})
        original_latex = latex_str
        normalized_latex = latex(expr)
        sympy_expr = srepr(expr)

        return {
            "hash": hash_value,
            "main_formula_tree": formula_tree,
            "formula_keywords": keywords,
            "original_latex": original_latex,
            "normalized_latex": normalized_latex,
            "sympy_expr": sympy_expr
        }

    except Exception as e:
        return {"error": str(e)}
