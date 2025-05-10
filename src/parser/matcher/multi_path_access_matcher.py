from node.path_access_node import PathAccessNode
from matcher.utils.dot_matcher import match as match_dot 
from matcher.identifier_matcher import match as match_identifier 

def match(tokens):
    steps = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        identifier = match_identifier(tokens[i:])
        if identifier:
            steps.append(identifier["node"])
            i += identifier.get("length", 1)

            if i < len(tokens) and match_dot(tokens[i:]):
                i += 1
            else:
                break
        else:
            break

    if steps and len(steps) > 1:
        return {
            "node": PathAccessNode(steps[:-1]),
            "length": i-1
        }

    return None