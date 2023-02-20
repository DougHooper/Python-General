# declare a running total to hold the total of numbers entered
total = 0
number = 1

while number > 0:
    number = int(input("Enter a number, enter a negative number or 0 to stop: "))

    if number > 0:
        total += number 

    print(f"Current total: {total}")