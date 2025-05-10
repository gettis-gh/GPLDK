import re

def match(input_str: str, i: int):
    # Verificamos si el carácter actual es una comilla doble "
    if input_str[i] in ('"', "'"):
        quote_char = input_str[i]
        start = i + 1  # Empezamos a capturar después de la comilla inicial
        i += 1
        
        # Capturamos todo lo que esté entre las comillas
        while i < len(input_str) and input_str[i] != '"':
            i += 1
        
        if i < len(input_str) and input_str[i] == quote_char:  # Si encontramos una comilla de cierre
            i += 1
            value = input_str[start:i-1]
            return {"type": "LITERAL", "value": value, "length": i - start + 1}
    
    return None
