
# The while loop

# syntax:

# while expression:
#     statement(s)

# example:

count = 0
while count < 9:
    print("The count is : ", count)
    count += 1

print("Good Bye!")

# here we saw that the block of code executed repeatedly until the count is no longer less than 9.

# The infinite loop

# a loop becomes infinite if the condition never turns to be False.

# example:
"""
var = 1
while var == 1:
    num = input("Enter a number: ")
    print("You entered: ", num)
print("Good Bye!")
"""
# Above example goes infinite loop and you need to use CTRL+C to exit the program.

# Using else statement with loops

# example:

count=0
while count < 5:
    print(count, " is less than 5.")
    count += 1
else:
    print(count, " is not less than 5.")
    
# Single Statement Suites
"""
flag = 1
while flag: print("Given falg is really True!")
print("Good Bye!")
"""
# the above code is an example of infinite loop too.
