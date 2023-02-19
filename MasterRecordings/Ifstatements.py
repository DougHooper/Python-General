# if statements are single alternative decision structures

'''
    structure of an if statement:

    if condition: 
        statement(s) if condition is true then execute the statement

    statements are going to execute only if the condition is true

    boolean expressions are built using relational operatos: 
        > greater than
        < less than
        >= greater than or equal to
        <= less than or equal to
        == is equal to (don't confuse with =)
        ! logical not (flips the value of a boolean expression)
        != is not equal to (flips the value of boolean expression)
        and - logical and (both sides have to be true for expression to be true)
        or - logical or

'''

number = int(input("Enter a number: "))

if number % 2 == 0:
     # % is the remainder after being divided by 2
    print("This number is even!")
    # this message only prints if the number is evenly divisible by 2

    # if statements are based off of indentation. as long as the statements are indented from the if statement, they will apply to the if statement being true

# if the condition is true then you do the statements to the rest of the program, if it's false it skips the statement. 

print(f"You entered the number: {number}")