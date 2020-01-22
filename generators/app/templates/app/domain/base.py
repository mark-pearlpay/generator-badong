from abc import ABC
from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseEntity(ABC):
    id: int
    created_timestamp: datetime
    last_modified_timestamp: datetime
