from datetime import datetime
from pprint import pprint
from unittest import TestCase
from unittest import main as unittest_main

from helpers import create_company, create_package, create_shipment, create_user
from reporting import Reporting


class TestReporting(TestCase):
    def setUp(self) -> None:
        self.kiu_company = create_company(company_name="Kiu", amount_of_shipments=0)
        self.another_company = create_company(company_name="Other", amount_of_shipments=2, amount_of_packages=3)

    def test_succeed_report(self):
        today = datetime.now().date()

        # so today there are 4 delivered shipments
        kiu_user = create_user(company_id=self.kiu_company.id)
        packages = [create_package(status="DELIVERED", cost=10.0) for _ in range(4)]
        self.kiu_company.shipments = [create_shipment(amount_of_packages=0, packages=packages)]

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


if __name__ == '__main__':
    unittest_main()
