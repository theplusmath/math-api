from sympy import sympify, latex, srepr
import hashlib

def normalize_latex(latex_str):
    try:
        expr = sympify(latex_str)

        # 1. hash
        hash_value = hashlib.sha256(latex_str.encode()).hexdigest()

        # 2. main_formula_tree (간단히 srepr로 대체 가능)
        formula_tree = srepr(expr)

        # 3. keywords (기초 버전)
        keywords = list({type(atom).__name__ for atom in expr.atoms()})

        # 4. original_latex
        original_latex = latex_str

        # 5. normalized_latex
        normalized_latex = latex(expr)

        # 6. sympy_expr
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
