from entities.company import Company


class Reporting:
    def generate_report(self, company: Company, date):
        delivered_shipments = company.get_delivered_packages_by_date(date)
        total_cost = sum([package.cost for package in delivered_shipments])
        return {
            "delivered_shipments": delivered_shipments,
            "total_cost": total_cost,
        }
