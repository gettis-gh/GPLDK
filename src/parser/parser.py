import os
import argparse
import json
from typing import List, Optional

from type.matcher_type import Matcher
from type.token_type import Token

from service.load_matchers_service import load_matchers
from service.parse_service import parse

matchers: List[Matcher] = []
load_matchers(matchers)

def main(tokens: List[Token], output: Optional[str] = None):
    # Llamada al parser para generar el AST
    ast = parse(tokens, matchers)
    
    if output:
        os.makedirs(os.path.dirname(output), exist_ok=True)
        with open(output, "w") as f:
            json.dump([node.to_dict() for node in ast], f, indent=2)  # Guardar el AST en un archivo JSON
    else:
        for node in ast:
            print(node)  # Mostrar el AST en consola

def read_tokens(file_path: str) -> List[Token]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)  # Se espera que los tokens estén en formato JSON
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"Error reading the token file: {e}")
        return []

def parse_arguments():
    parser = argparse.ArgumentParser(description="Parser CLI for generating AST from token list.")
    parser.add_argument('-f', '--file', type=str, required=True, help="Path to the token list (JSON format).")
    parser.add_argument('-o', '--output', type=str, help="Path to save the output AST as a JSON file.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    tokens = read_tokens(args.file)
    
    if not tokens:
        print("No tokens found. Exiting...")
        exit(1)
    
    main(tokens, output=args.output)
