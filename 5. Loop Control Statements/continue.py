
# continue statement rejects all the remaining satements
# in the current iteration of the loop and 
# moves the control back to the top of the loop.

# syntax:
# continue

# example:
for letter in 'Python':
    if letter == 'h':
        continue
    print("Current letter : ", letter)
    
# here we can see that the loop only skip the letter 'h' and prints all other letter.

# example:
var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print("current variable value: ", var)
    
print("Good Bye !")

# here we can see that the loop only skip the number 5 and prints all other numbers.
