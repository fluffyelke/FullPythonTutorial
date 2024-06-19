import datetime

day_expenses = {}

is_active = True
total_income_per_day = 0
while is_active:
    type_of_expense = input("Enter type of expense or 'quit' to exit: ")
    if type_of_expense.lower() == 'quit':
        is_active = False
        break

    money = 0
    spending_list = input("Enter Amount: ").split()
    for elem in spending_list:
        money += float(elem)

    day_expenses[type_of_expense] = money
    total_income_per_day += money

day_expenses['тотал'] = total_income_per_day

for exp_type, expenses in day_expenses.items():
    print(f"\t{exp_type.title(): >20}: {expenses: >10.2f} лв")

curr_year = datetime.datetime.now().year
curr_month_str = datetime.datetime.now().strftime('%B')
curr_day = datetime.datetime.now().day
month_expenses = {str(curr_day): day_expenses}

total_expenses = {
    str(curr_year): {
        curr_month_str: [],
    }
}
total_expenses.get(str(curr_year)).get(curr_month_str).append(month_expenses)

for year, year_items in total_expenses.items():
    print(f"\t{year}")
    for month, month_values in year_items.items():
        print(f"\t\t{month}")
        for elements in month_values:
            for day, element_vals in elements.items():
                print(f"\t\t\t{day}: ")
                for k, v in element_vals.items():
                    print(f"\t\t\t\t{k.title(): >20}: {v: >10.2f} лв")

