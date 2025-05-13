from matcher.third_grade.invocation_matcher import match as match_invocation
from matcher.first_grade.literal_matcher import match as match_literal

def match(tokens):
    return (
        match_invocation(tokens)
        or match_literal(tokens)
    )