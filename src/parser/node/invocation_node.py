from type.node_type import Node
from typing import List, Dict, Any
from node.path_access_node import PathAccessNode
from node.identifier_node import IdentifierNode
from node.literal_node import LiteralNode

class InvocationNode(Node):
    def __init__(self, pathAccess: PathAccessNode, invoker: IdentifierNode, arguments: List[Dict[str, Any]]):
        if not isinstance(pathAccess, PathAccessNode):
            raise ValueError("pathAccess debe ser una instancia de PathAccessNode")
        if not isinstance(invoker, IdentifierNode):
            raise ValueError("invoker debe ser una instancia de IdentifierNode")
        if not all(isinstance(arg['value'], (LiteralNode, InvocationNode)) for arg in arguments):
            raise ValueError("Cada valor en los argumentos debe ser una instancia de LiteralNode o InvocationNode")
        
        self.pathAccess = pathAccess
        self.invoker = invoker
        self.arguments = arguments

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "InvocationNode",
            "pathAccess": self.pathAccess.to_dict(),
            "invoker": self.invoker.to_dict(),
            "arguments": [
                {"name": arg["name"].to_dict(), "value": arg["value"].to_dict()} for arg in self.arguments
            ]
        }
