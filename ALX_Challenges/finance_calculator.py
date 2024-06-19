#User input for Financial Details:
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

#Calculating Monthly Savings
monthly_savings = float(monthly_income) - float(monthly_expenses)

#Projecting Annual Savings
simple_annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Outputting the results
print(f"Your monthly_savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}\n")