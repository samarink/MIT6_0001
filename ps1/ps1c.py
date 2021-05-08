portion_down_payment = 0.25
annual_return = 0.04
total_cost = 1_000_000
semi_annual_raise = 0.7
epsilon = 100

starting_salary = int(input('Enter your annual salary: '))
target_amount = total_cost * portion_down_payment

number_of_steps = 0

# the upper and lower bounds of search
low = 0
high = 10000

while True:
    annual_salary = starting_salary
    current_savings = 0

    portion_saved = ((low + high) / 2) / 10000  # as a float e.g 0.5
    monthly_saving = annual_salary / 12 * portion_saved

    # calculate how much can be saved given current portion_saved
    for month in range(0, 36):
        current_savings += (current_savings*annual_return/12) + monthly_saving

        # adjust by semi annual rise
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_saving = annual_salary / 12 * portion_saved

    # saved just enough? print and exit
    if abs(target_amount - current_savings) <= epsilon:
        print('Best savings rate:', round(portion_saved, 2), '%')
        print('Steps in bisection search', number_of_steps)
        break

    # saved more than necessary? lower the bar
    if current_savings > target_amount:
        high = portion_saved * 10000

    # saved less? raise the bar
    else:
        low = portion_saved * 10000

    # exhausted all posibilities? not possible to save
    if low >= high:
        print('It is not possible to pay the down payment in three years.')
        break

    number_of_steps += 1
