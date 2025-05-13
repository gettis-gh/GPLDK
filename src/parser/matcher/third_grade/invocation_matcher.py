from matcher.second_grade.path_matcher import match as match_path
from matcher.first_grade.identifier_matcher import match as match_identifier 
from matcher.second_grade.payload_matcher import match as match_payload 

from node.invocation_node import InvocationNode

def match(tokens):
    path = match_path(tokens)
    if path:
        index = 1 + path["length"]
        invoker = match_identifier(tokens[index:])
        if invoker:
            index += invoker["length"]
            payload = match_payload(tokens[index:])
            if payload:
                index += payload["length"]
                payload_node = payload["node"]
            else:
                payload_node = None
            return {
                "node": InvocationNode(path["node"], invoker["node"], payload_node),
                "length": index-1
            }
    return None