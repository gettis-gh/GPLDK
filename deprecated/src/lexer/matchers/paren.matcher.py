def match(input_str: str, i: int):
    if input_str[i] == "(":
        return {"type": "LPAREN", "value": "(", "length": 1}
    elif input_str[i] == ")":
        return {"type": "RPAREN", "value": ")", "length": 1}
    return None