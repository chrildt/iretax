class TaxCalculator:

    def __init__(self, income, marital_status, both_earning=False, single_parent=False):
        self.income = income
        self.marital_status = marital_status
        self.both_earning = both_earning
        self.single_parent = single_parent
        self.tax_deducted = 0
        self.usc_deducted = 0

    def calculate_tax(self):
        # Determine tax brackets based on user's situation
        if self.marital_status == 'single':
            if self.single_parent:
                rate_bracket = 48000
            else:
                rate_bracket = 44000
        elif self.marital_status == 'married':
            rate_bracket = 53000
            if self.both_earning:
                rate_bracket += min(self.income, 35000)
        else:
            print("Invalid marital status. Please enter either 'single' or 'married'.")
            return

        # Calculate tax
        if self.income <= rate_bracket:
            self.tax_deducted = self.income * 0.20
        else:
            self.tax_deducted = rate_bracket * 0.20 + (self.income - rate_bracket) * 0.40

        return self.tax_deducted

    def calculate_usc(self):
        # Calculate Universal Social Charge
        if self.income <= 12012:
            self.usc_deducted = self.income * 0.005
        elif self.income <= 27382:  # 12012 + 15370
            self.usc_deducted = 12012 * 0.005 + (self.income - 12012) * 0.02
        elif self.income <= 70044:  # 27382 + 42662
            self.usc_deducted = 12012 * 0.005 + 15370 * 0.02 + (self.income - 27382) * 0.03
        else:
            self.usc_deducted = 12012 * 0.005 + 15370 * 0.02 + 42662 * 0.03 + (self.income - 70044) * 0.08

        return self.usc_deducted

    def calculate_net_income(self):
        self.calculate_tax()
        self.calculate_usc()
        deductions = self.tax_deducted + self.usc_deducted
        net_annual_income = round(self.income - deductions)  # Rounded to nearest whole number
        net_monthly_income = round(net_annual_income / 12)  # Rounded to nearest whole number
        return net_annual_income, net_monthly_income
