def calculate(expression: str) -> float:
    # Validar entrada vacía o solo espacios
    if expression is None or expression.strip() == "":
        raise ValueError("Input is empty or only whitespace")

    # Validar caracteres permitidos (números, operadores, paréntesis, puntos, espacios)
    import re
    if not re.fullmatch(r"[0-9\.\+\-\*/\(\)\s]+", expression):
        raise ValueError("Invalid character in expression")

    try:
        # Evaluar la expresión de forma segura
        result = eval(expression, {"__builtins__": None}, {})
    except ZeroDivisionError:
        raise
    except SyntaxError:
        raise SyntaxError("Invalid syntax in expression")
    except Exception:
        raise ValueError("Invalid expression")

    return result