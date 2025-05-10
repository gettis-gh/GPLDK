from type.node_type import Node
from typing import Dict, Any

class DotNode(Node):
    def to_dict(self) -> Dict[str, Any]:
        return {"type": "DotNode"}