from type.node_type import Node
from typing import Dict, Any

class ColonNode(Node):
    def to_dict(self) -> Dict[str, Any]:
        return {"type": "ColonNode"}