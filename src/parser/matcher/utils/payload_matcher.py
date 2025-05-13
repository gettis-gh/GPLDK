def match(tokens):
    from matcher.utils.expression_matcher import match as match_expression

    params = []
    index = 0
    paren_opened = False

    if index < len(tokens) and tokens[index]["type"] == "LPAREN":
        paren_opened = True
        index += 1

    while index < len(tokens) and paren_opened:
        if tokens[index]["type"] == "RPAREN":
            paren_opened = False
            break

        if tokens[index]["type"] == "COLON" or tokens[index]["type"] == "COMMA":
            index += 1
            continue

        if index + 1 < len(tokens) and tokens[index + 1]["type"] == "COLON":
            name = tokens[index]["value"]
            index += 2

            value = match_expression(tokens[index:])
            if value:
                params.append({"name": name, "value": value["node"]})
                index += value["length"]
                continue
            else:
                break
        else:
            index += 1

    if len(params) > 0:
        return {"node": params, "length": index}

    return None
