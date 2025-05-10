def match(input_str: str, i: int):
    if input_str[i].isalpha():
        start = i
        while i < len(input_str) and (input_str[i].isalnum() or input_str[i] == "_"):
            i += 1
        return {"type": "IDENTIFIER", "value": input_str[start:i], "length": i - start}
    return None