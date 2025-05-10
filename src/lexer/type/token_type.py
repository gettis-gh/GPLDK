# token.type.py
from typing import TypedDict, Optional

class Token(TypedDict, total=False):
    type: Optional[str]
    value: Optional[str]
    length: int
    line: int
    column: int
    skip: bool