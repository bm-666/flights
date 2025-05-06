from dataclasses import dataclass, field
from typing import Any

@dataclass
class HttpResponse:
    status_code: int
    json_data: Any | None = None
    text: str = ""
    headers: dict[str, str] | None = field(default_factory=dict)