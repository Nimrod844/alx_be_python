monthly_income = float(input("Enter you monthly income: "))
monthly_expenses = float(input("enter you total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05 )
print(f"your monthly savings are ${monthly_savings:.2f}.")
print(f"projected savings after one year , with interest,is: ${projected_savings:.2f}. ")