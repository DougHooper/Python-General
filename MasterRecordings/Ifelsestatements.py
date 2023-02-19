"""
    if / else statemetns are known as dual alternative decision structures

        structure: 

            if condition: 
                statemetn(s)
            else: 
                statement(s)

        No need to put conditions on the else block
        python understands that the else is the condition tha tthe if is false
"""

number = int(input("Enter a number: "))

# if/else statement that displays a message if the numebr is even or odd
if number % 2 == 0:
    print("This number is even")

else:
    print("This number is odd")

print(f"You entered the number: {number}")