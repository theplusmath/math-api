import hashlib

def normalize_latex(latex: str) -> str:
    normalized = latex.replace(" ", "")
    hash_value = hashlib.sha256(normalized.encode()).hexdigest()
    return hash_value
