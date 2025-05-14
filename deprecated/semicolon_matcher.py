def match(input_str: str, i: int):
    if input_str[i] == ";":
        return {
            "type": "SEMICOLON", 
            "value": ";", 
            "length": 1
            }
    return None