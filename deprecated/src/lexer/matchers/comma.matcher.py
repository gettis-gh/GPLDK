def match(input_str: str, i: int):
    if input_str[i] == ",":
        return {"type": "COMMA", "value": ",", "length": 1}
    return None