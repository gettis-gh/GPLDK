def match(input_str: str, i: int):
    if input_str[i] in " \t\n":
        start = i
        length = 1
        while i + length < len(input_str) and input_str[i + length] in " \t\n":
            length += 1
        return {
            "type": "WHITESPACE", 
            "value": input_str[start:i], 
            "length": length,
            "skip": True
        }
    return None