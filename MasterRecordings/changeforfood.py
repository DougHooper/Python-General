# ask the user to enter the charge for the food
mealcost = float(input("How much was your meal? $"))

# calcualte the tip
tip = mealcost * 0.15

salestax = mealcost * 0.07

# calcualte the total
mealtotal = mealcost + tip + salestax 

print(f"Total: ${mealtotal:,.2f}")