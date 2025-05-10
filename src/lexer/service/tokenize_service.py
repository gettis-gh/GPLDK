from type.matcher_type import Matcher
from type.token_type import Token
from typing import List
import sys

def tokenize(input_str: str, matchers) -> List[Token]:
    index = 0
    tokens: List[Token] = []
    line = 1
    column = 1
    
    while index < len(input_str):
        for matcher in matchers:
            result = matcher(input_str, index)

            if result:
                if result.get("length", 0) == 0:
                    raise RuntimeError(f"Matcher returned length=0 at index {index}, line {line}, column {column}")

                if result.get("skip", False):
                    for _ in range(result["length"]):
                        if input_str[index] == "\n":
                            line += 1
                            column = 1
                        else:
                            column += 1
                        index += 1
                    break
                else:
                    result["line"] = line
                    result["column"] = column
                    tokens.append(result)

                    for _ in range(result["length"]):
                        if input_str[index] == "\n":
                            line += 1
                            column = 1
                        else:
                            column += 1
                        index += 1
                    break
        else:
            # Obtener línea completa para vista previa
            line_start = index
            while line_start > 0 and input_str[line_start - 1] != "\n":
                line_start -= 1

            line_end = index
            while line_end < len(input_str) and input_str[line_end] != "\n":
                line_end += 1

            line_content = input_str[line_start:line_end]
            pointer = " " * (column - 1) + "^"
            
            print("Lexical Error:")
            print(f"  → Unexpected character '{input_str[index]}' at line {line}, column {column}")
            print(f"    {line_content}")
            print(f"    {pointer}")
            sys.exit(1)

    return tokens
