from type.node_type import Node
from typing import Dict, Any

class LiteralNode(Node):
    def __init__(self, value: str):
        self.value = value
    
    def to_dict(self) -> Dict[str, Any]:
        return {"type": "LiteralNode", "value": self.value}