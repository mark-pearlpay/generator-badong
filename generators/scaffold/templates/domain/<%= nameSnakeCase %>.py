from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class <%= namePascalCase %>(ABC):
	id: int
	name: str
	duration: int
	view_count: int
