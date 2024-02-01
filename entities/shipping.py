from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Union
from uuid import UUID

from constants import ShipmentStatus
from entities.user import User


@dataclass
class Package:
    id: UUID
    user_id: UUID
    name: str
    weight: float
    timestamp: datetime = field(default_factory=datetime.now)
    status: Union[
        ShipmentStatus,
        None,
    ] = field(default=None)
    cost: float = field(default=0.0)

    def change_status(self, status: Union[ShipmentStatus, None]) -> None:
        self.status = status
        self.timestamp = datetime.now()


@dataclass
class Shipment:
    id: UUID
    users: List[User]
    packages: List[Package]
    origin: str
    destination: str

    @property
    def weight(self) -> float:
        return sum([package.weight for package in self.packages])

    def get_delivered_packages(self) -> List[Package]:
        return [package for package in self.packages if package.status == ShipmentStatus.DELIVERED]

    def get_delivered_packages_by_date(self, date: datetime) -> List[Package]:
        packages = self.get_delivered_packages()
        return [package for package in packages if package.timestamp.date() == date]

    def get_total_delivered_cost(self) -> float:
        return sum([package.cost for package in self.get_delivered_packages()])
