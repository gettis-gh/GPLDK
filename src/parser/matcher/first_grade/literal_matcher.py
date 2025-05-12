from node.literal_node import LiteralNode

def match(tokens):
    if not tokens:
        return None

    token = tokens[0]
    if token["type"] == "LITERAL":
        return {
            "node": LiteralNode(token["value"]),
            "length": 1
        }
    return None