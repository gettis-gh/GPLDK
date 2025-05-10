from type.node_type import Node
from typing import List, Dict, Any
from node.identifier_node import IdentifierNode 

class PathAccessNode(Node):
    def __init__(self, steps: List[Node]):
        if not all(isinstance(step, IdentifierNode) for step in steps):
            raise ValueError("Todos los pasos deben ser instancias de IdentifierNode")
        self.steps = steps

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "PathAccessNode",
            "steps": [step.to_dict() for step in self.steps]
        }