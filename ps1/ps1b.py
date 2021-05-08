portion_down_payment = 0.25
current_savings = 0
annual_return = 0.04

annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(
    input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi anual rise, as a decimal: '))


monthly_saving = annual_salary / 12 * portion_saved
target_amount = total_cost * portion_down_payment


number_of_months = 0

while current_savings < target_amount:
    current_savings += (current_savings*annual_return/12) + monthly_saving
    number_of_months += 1

    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_saving = annual_salary / 12 * portion_saved

print('Number of months', number_of_months)
