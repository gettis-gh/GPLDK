from node.identifier_node import IdentifierNode

def match(tokens):
    if not tokens:
        return None

    token = tokens[0]
    if token["type"] == "IDENTIFIER":
        return {
            "node": IdentifierNode(token["value"]),
            "length": 1
        }
    return None