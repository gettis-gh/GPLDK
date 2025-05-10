def match(input_str: str, i: int):
    if input_str[i] == ":":
        return {
            "type": "COLON", 
            "value": ":", 
            "length": 1
        }
    return None