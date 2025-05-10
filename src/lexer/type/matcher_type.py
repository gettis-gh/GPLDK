from typing import Callable, Optional
from type.token_type import Token

Matcher = Callable[[str, int], Optional[Token]]