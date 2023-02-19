# use the input value to be used for a calculation later on, convert the input value to a number by type casting as Int or float

TotalSales = float(input("Enter the projected total sales: $ "))

# calcualte the profit (23%)
profit = TotalSales * 0.23

# display the total sales
print(f"Total sales: ${TotalSales:,.2f}")

print(f"profit: ${profit:,.2f}")

