from dataclasses import dataclass

from domain import BaseEntity

@dataclass
class <%= namePascalCase %>(BaseEntity):
	name: str
	duration: int
	view_count: int
