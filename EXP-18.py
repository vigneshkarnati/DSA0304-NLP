import re

def parse_fopc(expression):
    expression = expression.strip()

    # Pattern for simple predicate:
    # P(x), P(a), Loves(x,y), etc.
    pattern = r'^[A-Za-z][A-Za-z0-9_]*\s*\(\s*[a-zA-Z][a-zA-Z0-9_]*(\s*,\s*[a-zA-Z][a-zA-Z0-9_]*)*\s*\)$'

    # Handle NOT
    if expression.startswith("NOT "):
        expression = expression[4:].strip()

    # Handle AND / OR
    if " AND " in expression:
        parts = expression.split(" AND ")
        return all(parse_fopc(part) for part in parts)

    if " OR " in expression:
        parts = expression.split(" OR ")
        return any(parse_fopc(part) for part in parts)

    # Handle simple predicate
    return bool(re.match(pattern, expression))


expressions = [
    "Human(x)",
    "Loves(x,y)",
    "Human(x) AND Loves(x,y)",
    "NOT Human(x)",
    "Human(x) AND"
]

for expression in expressions:
    if parse_fopc(expression):
        print(expression, "-> Valid FOPC expression")
    else:
        print(expression, "-> Invalid FOPC expression")