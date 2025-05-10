from lexer.tokenizer import tokenize

# Leer el archivo main.gs
with open("main.gl", "r") as f:
    code = f.read()

# Tokenizar el código leído
tokens = tokenize(code)

# Imprimir los tokens
for token in tokens:
    print(token)