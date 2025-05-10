from node.comma_node import CommaNode

def match(tokens):
    if not tokens:
        return None

    token = tokens[0]
    if token["type"] == "COMMA":
        return {
            "node": CommaNode(),
            "length": 1
        }
    return None