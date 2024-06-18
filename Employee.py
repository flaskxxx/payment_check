class Employee:
    def __init__(self, salary:float,
                 work_days: int = 0,
                 work_hours: int = 0,
                 tax_rate: int = 0,
                 bonus: float = 0.0,
                 weekend_money: float = 0.0,
                 business_trip_money: float = 0.0,
                 academy: float = 0.0,
                 plus: float = 0.0):
        self.salary = salary
        self.work_days = work_days
        self.work_hours = work_hours
        self.tax_rate = tax_rate
        self.bonus = bonus
        self.weekend_money = weekend_money
        self.business_trip_money = business_trip_money
        self.academy = academy
        self.plus = plus
        self.salary_taxes = 0.0
        self.academy_taxes = 0.0
        self.business_trip_money_taxes = 0.0
        self.weekend_money_taxes = 0.0
        self.pluses_taxes = 0.0
        self.bonuses_taxes = 0.0
        self.all_taxes: float = 0.0
        self.do_taxes()
        self.total_invoice = self.get_total_invoice()
        self.salary_w_taxes: float = self.total_invoice + self.all_taxes

    def count_taxes(self, amount):
        return (amount / 100) * self.tax_rate

    def get_total_invoice(self):
        return self.salary + self.bonus + self.business_trip_money

    def do_taxes(self):
        self.weekend_money_taxes = self.count_taxes(self.weekend_money)
        self.academy_taxes = self.count_taxes(self.academy)
        self.pluses_taxes = self.count_taxes(self.plus)
        self.salary_taxes = self.count_taxes(self.salary)
        self.bonuses_taxes = self.count_taxes(self.bonus)
        self.business_trip_money_taxes = self.count_taxes(self.business_trip_money)
        self.all_taxes = (self.salary_taxes
                          + self.bonuses_taxes
                          + self.business_trip_money_taxes)
