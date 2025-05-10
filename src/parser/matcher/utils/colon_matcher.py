from node.colon_node import ColonNode

def match(tokens):
    if not tokens:
        return None

    token = tokens[0]
    if token["type"] == "COLON":
        return {
            "node": ColonNode(),
            "length": 1
        }
    return None