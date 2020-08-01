
# syntax:

# if expression1:
#     statement(s)
# elif expression2:
#     statement(s)
# elif expression3:
#     statement(s)
# elif expression4:
#     statement(s)
# else:
#     statement(s)

# here when the expression checking starts from top the block with the expression getting true
# will get executed and rest of the blocks below it will not even get checked and the statement ends.

# example:

var = 100
if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)
elif var == 100:
    print("3 - Got a true expression value")
    print(var)
elif var == 500:
    print("4 - Got a true expression value")
    print(var)
else:
    print("5 - Got a true expression value")
    print(var)

print("Good Bye !")

# here we can see that the exressions are checked from top,
# and when the expression was true in the third block the result in that block get printed 
# this not even checked for the below expressions
