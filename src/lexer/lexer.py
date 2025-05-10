import os
import importlib.util
import argparse
from typing import List, Callable, Optional

from type.matcher_type import Matcher
from type.token_type import Token

from service.load_matchers_service import load_matchers
from service.tokenize_service import tokenize

matchers: List[Matcher] = []
load_matchers(matchers)

def main(input_str: str, output: Optional[str] = None):
    tokens = tokenize(input_str, matchers)
    
    if output:
        import json, os
        os.makedirs(os.path.dirname(output), exist_ok=True)
        with open(output, "w") as f:
            json.dump(tokens, f, indent=2)
    else:
        for token in tokens:
            print(token)

def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return ""
    except Exception as e:
        print(f"Error reading the file: {e}")
        return ""

def parse_arguments():
    parser = argparse.ArgumentParser(description="Lexer CLI for tokenizing strings or files.")
    parser.add_argument('-f', '--file', type=str, help="Path to the .gt file to tokenize.")
    parser.add_argument('-o', '--output', type=str, help="Path to save the output tokens as a JSON file.")
    parser.add_argument('input', nargs='?', type=str, help="The string to tokenize. Optional if a file is provided.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    
    if args.file:
        input_str = read_file(args.file)
    elif args.input:
        input_str = args.input
    else:
        print("You must provide either a string or a file to tokenize.")
        exit(1)
    
    main(input_str, output=args.output)  # Aquí pasas `args.output`
