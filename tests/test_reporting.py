from datetime import datetime
from pprint import pprint
from unittest import TestCase
from unittest import main as unittest_main
from uuid import uuid4

from helpers import create_company, create_package, create_shipment, create_user
from reporting import Reporting


class TestReporting(TestCase):
    def setUp(self) -> None:
        self.kiu_company = create_company(company_name="Kiu", amount_of_shipments=0)
        self.another_company = create_company(company_name="Other", amount_of_shipments=2, amount_of_packages=3)
        self.kiu_users = [create_user(company_id=self.kiu_company.id) for _ in range(3)]

    def test_succeed_report(self):
        today = datetime.now().date()
        kiu_user = self.kiu_users[0]

        # so today there are 4 delivered shipments for a kiu user with a cost of 10.0 each
        packages = [
            create_package(name="PlayStation 5", status="DELIVERED", user_id=kiu_user.id, cost=10.0) for _ in range(4)
        ]
        self.kiu_company.shipments = [create_shipment(users=[kiu_user], amount_of_packages=0, packages=packages)]

        reporting = Reporting()
        report = reporting.generate_report(self.kiu_company, today)
        pprint(report)
        self.assertEqual(report["total_cost"], 40.0)

    def test_no_delivered_shipments(self):
        today = datetime.now().date()

        reporting = Reporting()
        report = reporting.generate_report(self.kiu_company, today)
        pprint(report)
        self.assertEqual(report["total_cost"], 0.0)

    def test_bulk_users_but_only_20_in_the_company(self):
        today = datetime.now().date()
        hundred_users = [create_user(company_id=uuid4()) for _ in range(100)]
        twenty_users = hundred_users[:20]
        # so today there are 20 kiu users that have 4 delivered shipments with a cost of 10.0 each each one
        for user in twenty_users:
            user.company_id = self.kiu_company.id
            packages = [
                create_package(name="PlayStation 5", status="DELIVERED", user_id=user.id, cost=10.0) for _ in range(4)
            ]
            self.kiu_company.shipments += [create_shipment(users=[user], amount_of_packages=0, packages=packages)]

        reporting = Reporting()
        report = reporting.generate_report(self.kiu_company, today)
        pprint(report)
        self.assertEqual(report["total_cost"], 800.0)  # 20 users * 4 shipments * 10.0 cost each


if __name__ == '__main__':
    unittest_main()
