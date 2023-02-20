# while loops can also be used to validate input validation
repeat = int(input("Enter a value between 1 and 5: "))

while repeat < 1 or repeat > 5: 
    print("number entered is out of range of 1-5. try again")

    repeat = int(input("enter a value between 1 and 5: "))

while repeat > 0:
    print("This is python")
    repeat -= 1