from node.path_access_node import PathAccessNode
from node.identifier_node import IdentifierNode
from node.invocation_node import InvocationNode

from matcher.identifier_matcher import match as match_identifier
from matcher.literal_matcher import match as match_literal

from matcher.utils.dot_matcher import match as match_dot
from matcher.utils.colon_matcher import match as match_colon
from matcher.utils.comma_matcher import match as match_comma

def match(tokens):
    steps = []
    i = 0

    # Procesar el path
    while i < len(tokens):
        token = tokens[i]

        # Intentar hacer match con un identificador
        identifier = match_identifier(tokens[i:])
        if identifier:
            steps.append(identifier["node"])
            i += identifier.get("length", 1)

            # Si encontramos un punto, seguimos procesando
            if i < len(tokens) and match_dot(tokens[i:]):
                i += 1
            else:
                break
        else:
            break

    # Si hay pasos, excluimos el último como invocador
    if steps and len(steps) > 1:
        path_access_node = PathAccessNode(steps[:-1])
        invoker = steps[-1]

        # Ahora, manejamos los parámetros entre paréntesis
        if i < len(tokens) and tokens[i]["value"] == "(":
            i += 1  # Pasar el paréntesis de apertura
            arguments = []

            # Procesar argumentos dentro de los paréntesis
            while i < len(tokens) and tokens[i]["value"] != ")":
                # Argumento: name: value
                name_token = match_identifier(tokens[i:])
                if name_token:
                    name_node = name_token["node"]
                    i += name_token.get("length", 1)

                    # Colon
                    if i < len(tokens) and match_colon(tokens[i:]):
                        i += 1

                    # Value (puede ser literal o invocación)
                    value_token = match_literal(tokens[i:])
                    if not value_token:
                        # Si no es un literal, puede ser otra invocación (recursiva)
                        value_token = match(tokens[i:])

                    if value_token:
                        arguments.append({
                            "name": name_node,
                            "value": value_token["node"]
                        })
                        i += value_token.get("length", 1)

                    # Comma para separar argumentos
                    if i < len(tokens) and match_comma(tokens[i:]):
                        i += 1
                else:
                    break
            if i < len(tokens) and tokens[i]["value"] == ")":
                i += 1  # Pasar el paréntesis de cierre

        return {
            "node": InvocationNode(path_access_node, invoker, arguments),
            "length": i
        }

    return None
