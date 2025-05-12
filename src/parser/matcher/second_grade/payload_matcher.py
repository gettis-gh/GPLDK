def match(tokens):
    from matcher.third_grade.invocation_matcher.py import match as match_invocation
    
    arguments = {}
    index = 0
    paren_opened = false
    if tokens[index].type == "LPAREN":
        paren_opened = true
        index += 1
    while index < len(tokens) and paren_opened:
        if tokens[index].type == "RPAREN":
            paren_opened = false
            break
        
        invocation = match_invocation(tokens[index:])
        if invocation:
            
            continue
        