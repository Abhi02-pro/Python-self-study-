
# syntax:

# if expression:
#     statement(s)
# else:
#     statement(s)

# here if the expression of the if statement turns out to be false
# the the block of statement(s) in else will get executed

# example:

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)
else:
    print("1 - Got a false expression value")
    print(var1)

var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)
else:
    print("2 - Got a false expression value")
    print(var2)

print("Good Bye !")

# when we run the above code we can observe that 
# in the first set of if-else statement the if block executed as var1 is non-zero and not-null
# in the next set of if-else statement the else block get executed as var2 is zero