def match(input_str: str, i: int):
    if input_str[i] == ".":
        return {
            "type": "DOT", 
            "value": ".", 
            "length": 1
        }
    return None