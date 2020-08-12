
# break statement terminates the execution of the current loop and 
# resume execution at the next statement, 
# just like the traditional break statement in C.
# break statement can be used in both for and while Loop.

# If you are using nested loops, 
# the break statement stop the execution of the innermost loop and 
# start executing the next line of code after the block.

# syntax:
# break

# example:

for letter in "Python":
    if letter == "h":
        break
    print("Current letter :", letter)

# here we can see that the loop only runs till the letter 't' and breaks.
    
# example:

var = 10
while var > 0:
    print("Current variable value:", var)
    var -= 1
    if var == 5:
        break

print("Good Bye")

# here we can see that the loop only runs till the number 6 and breaks.