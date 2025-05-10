from type.node_type import Node
from type.node_type import Node
from typing import Dict, Any

class IdentifierNode(Node):
    def __init__(self, name: str):
        self.name = name
    
    def to_dict(self) -> Dict[str, Any]:
        return {"type": "IdentifierNode", "name": self.name}