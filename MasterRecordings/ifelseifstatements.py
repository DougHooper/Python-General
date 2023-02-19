# if / else if

"""
    multiple alternative decision structures are our if/else if statments:

    structure of an if/else if:

        if condition:
            statements
        elif condition:
            statements
        elif condition:
            statements
        else:
            statements

    You can have as many else ifs in between an if and an else as you need
"""

# have the user enter a number
a = int(input("enter a number: "))

b = int(input("enter another number: "))

if a > b:
    print(f"{a} is greater than {b}")

elif b > a:
    print(f"{b} is greater than {a}")

else: 
    print(f"{a} is equal to {b}")
