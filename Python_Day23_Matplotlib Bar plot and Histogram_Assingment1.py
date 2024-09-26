import matplotlib.pyplot as plt

# 1. Create a bar chart to represent monthly expenses in different spending categories.
#    - What are the categories of expenses?
#    - What are the monthly expenses in dollars for each category?
#    - What conclusions can be drawn from the chart?

# Input data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color='skyblue')
plt.title('Monthly Expenses by Category')
plt.xlabel('Spending Categories')
plt.ylabel('Expenses in Dollars')
plt.grid(axis='y')

# Show the plot
plt.show()

# Conclusion
total_expenses = sum(expenses)
print(f'Total Monthly Expenses: ${total_expenses}')
max_expense = max(expenses)
max_expense_category = categories[expenses.index(max_expense)]
print(f'Most significant expense is on {max_expense_category} (${max_expense})')
