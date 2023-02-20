# repition sturcture
"""
    While loops are pretest loops: checks to see if a condition is true to execute and repeat a series of statements and repeat the series of statemetns while the condition is true

    structure: 

        while condition: 
            statement(s):

    at least one of the statements needs to udpate the condition - needs to have a means to make the condition false
    if you don't you can create an infite loop

    while loops can execute from 0 up to many times

    while loops structure is similar to an if statement except for the worrd 'if' it has the word 'while'
"""

# loop control variable
repeat = 5 

while repeat > 0:
    print("this is python")

    # control + c to make an infinite loop stop

    # update the condiiton by changing the value of repeat
    repeat = repeat - 1

    #combined assignment

    repeat -=1 #same thing as saying repeat = repeat -1 and avoids typing the variable on each side of equal sign

    # avoid updating the value of the loop contorl variable multilpes times inside a block of code

    