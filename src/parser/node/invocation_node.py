from type.node_type import Node
from typing import List, Dict, Any
from node.path_node import PathAccessNode
from node.identifier_node import IdentifierNode
from node.literal_node import LiteralNode

class InvocationNode(Node):
    def __init__(self, path: PathAccessNode, invoker: IdentifierNode, arguments: List[Dict[str, Any]] = None):
        if not isinstance(path, PathAccessNode):
            raise ValueError("pathAccess debe ser una instancia de PathAccessNode")
        if not isinstance(invoker, IdentifierNode):
            raise ValueError("invoker debe ser una instancia de IdentifierNode")
        
        self.arguments = arguments or []

        self.path = path
        self.invoker = invoker

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "InvocationNode",
            "path": self.path.to_dict(),
            "invoker": self.invoker.to_dict(),
            "payload": [
                {"name": arg["name"], "value": arg["value"].to_dict()} for arg in self.arguments
            ]
        }
