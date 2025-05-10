import os
import importlib.util

def load_matchers():
    matchers = []
    matcher_dir = os.path.join(os.path.dirname(__file__), "matchers")

    for fname in os.listdir(matcher_dir):
        if fname.endswith(".matcher.py"):
            path = os.path.join(matcher_dir, fname)
            spec = importlib.util.spec_from_file_location(fname, path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            matchers.append(mod.match)
    return matchers

def load_filters():
    filters = []
    matcher_dir = os.path.join(os.path.dirname(__file__), "matchers")

    for fname in os.listdir(matcher_dir):
        if fname.endswith(".filter.py"):
            path = os.path.join(matcher_dir, fname)
            spec = importlib.util.spec_from_file_location(fname, path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            filters.append(mod.match)
    return filters

matchers = load_matchers()
filters = load_filters()

def tokenize(input_str: str):
    tokens = []
    i = 0
    line = 1
    column = 1

    while i < len(input_str):
        # Intentar aplicar filtros
        for f in filters:
            result = f(input_str, i)
            if result:
                for _ in range(result["length"]):
                    if input_str[i] == "\n":
                        line += 1
                        column = 1
                    else:
                        column += 1
                    i += 1
                break
        else:
            # Si ningún filtro se aplicó, intentar aplicar un matcher
            for matcher in matchers:
                result = matcher(input_str, i)
                if result:
                    result["line"] = line
                    result["column"] = column
                    tokens.append(result)

                    for _ in range(result["length"]):
                        if input_str[i] == "\n":
                            line += 1
                            column = 1
                        else:
                            column += 1
                        i += 1
                    break
            else:
                raise SyntaxError(f"Caracter inesperado: {input_str[i]} en posición {i}, línea {line}, columna {column}")
    return tokens
