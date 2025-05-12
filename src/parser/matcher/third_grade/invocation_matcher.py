from matcher.second_grade.path_matcher import match as match_path
from matcher.first_grade.identifier_matcher import match as match_identifier 
from matcher.second_grade.payload_matcher import match as match_payload 

from node.InvocationNode import InvocationNode

def match(tokens):
    path = match_path(tokens)
    if path:
        index = 1 + path.length
        invoker = match_identifier(tokens[index:])
        if identifier:
            index += invoker.length
            payload = match_payload(tokens[index:])
            return InvocationNode(path, invoker, payload)
    return None