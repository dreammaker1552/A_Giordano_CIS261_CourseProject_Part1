def get_employee_name():
    return input("Enter employee name: ")

def get_total_hours():
    return float(input("Enter total hours worked: "))

def get_hourly_rate():
    return float(input("Enter hourly rate: "))

def get_tax_rate():
    return float(input("Enter income tax rate (as decimal): "))

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    return gross_pay, tax, net_pay

def display_employee_pay(name, hours, rate, gross_pay, tax_rate, tax, net_pay):
    print("Employee name:", name)
    print("Total hours:", hours)
    print("Hourly rate:", rate)
    print("Gross pay:", gross_pay)
    print("Income tax rate:", tax_rate)
    print("Income tax:", tax)
    print("Net pay:", net_pay)

def display_summary(num_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    print("Number of employees:", num_employees)
    print("Total hours:", total_hours)
    print("Total gross pay:", total_gross_pay)
    print("Total tax:", total_tax)
    print("Total net pay:", total_net_pay)

num_employees = 0
total_hours = 0
total_gross_pay = 0
total_tax = 0
total_net_pay = 0

while True:
    name = get_employee_name()
    if name == "End":
        break
    hours = get_total_hours()
    rate = get_hourly_rate()
    tax_rate = get_tax_rate()
    gross_pay, tax, net_pay = calculate_pay(hours, rate, tax_rate)
    display_employee_pay(name, hours, rate, gross_pay, tax_rate, tax, net_pay)
    num_employees += 1
    total_hours += hours
    total_gross_pay += gross_pay
    total_tax += tax
    total_net_pay += net_pay

display_summary(num_employees, total_hours, total_gross_pay, total_tax, total_net_pay)

