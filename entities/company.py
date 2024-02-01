from dataclasses import dataclass, field
from datetime import datetime
from pprint import pprint
from typing import List
from uuid import UUID, uuid4

from entities.shipping import Package, Shipment


@dataclass
class Company:
    id: UUID = field(default_factory=uuid4)
    name: str
    shipments: List[Shipment]

    def get_delivered_packages_by_date(self, date: datetime) -> List[Package]:
        return [package for shipment in self.shipments for package in shipment.get_delivered_packages_by_date(date)]

    def __repr__(self) -> str:
        return pprint(self.__dict__)
