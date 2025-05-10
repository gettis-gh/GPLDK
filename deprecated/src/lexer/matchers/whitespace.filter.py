def match(input_str: str, i: int):
    if input_str[i] in " \t\n":
        length = 1
        while i + length < len(input_str) and input_str[i + length] in " \t\n":
            length += 1
        return {"length": length}
    return None