def match(input_str: str, i: int):
    if input_str[i] in ('"', "'"):
        quote_char = input_str[i]
        start = i
        i += 1

        while i < len(input_str) and input_str[i] != quote_char:
            i += 1

        if i < len(input_str) and input_str[i] == quote_char:
            i += 1
            return {
                "type": "LITERAL",
                "value": input_str[start + 1:i - 1],
                "length": i - start
            }

    return None