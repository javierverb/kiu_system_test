from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class User:
    id: UUID
    company_id: UUID
    username: str
    email: str
    password: str
    is_active: bool

    def __post_init__(self):
        self.id = uuid4()
