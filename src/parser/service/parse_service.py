from typing import List
import sys

def parse(tokens: List[dict], matchers: list):
    index = 0
    nodes = []

    while index < len(tokens):
        for matcher in matchers:
            result = matcher(tokens[index:])

            if result:
                node = result.get("node")
                length = result.get("length", 0)

                if not node or length == 0:
                    raise RuntimeError(f"Parser matcher returned invalid result at token index {index}")

                nodes.append(node)
                index += length
                break
        else:
            token = tokens[index]
            print("Syntax Error:")
            print(f"  → Unexpected token '{token['value']}' ({token['type']}) at line {token['line']}, column {token['column']}")
            sys.exit(1)

    return nodes