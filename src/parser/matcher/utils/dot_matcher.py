from node.dot_node import DotNode

def match(tokens):
    if not tokens:
        return None

    token = tokens[0]
    if token["type"] == "DOT":
        return {
            "node": DotNode(),
            "length": 1
        }
    return None