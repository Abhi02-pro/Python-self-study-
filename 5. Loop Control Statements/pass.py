
# It is used when the statement is required syntactally but you do not want any command or code to execute.
# The paas statement is a null operation.
# nothing happens when pass statement executes

# syntax:
# pass

# example:

for letter in "Python":
    if letter == "h":
        pass
        print("This is pass block.")
    print("Current letter: ", letter)
    
print("Good Bye!")

# pass is helpful when you test some empty module.