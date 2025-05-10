from typing import Dict, Any

class Node:
    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError("Each node has to implement its to_dict method.")