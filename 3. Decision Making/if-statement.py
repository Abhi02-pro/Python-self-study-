

# syntax:

# if expression:
#     statement(s)

# here if the boolean expression evaluates to TRUE, then block of statement(s) will get executed.

# examples:

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)

var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)

print("Good Bye !")

# so when we run this code we can see that only the first if statement got executed
# and not the second one, as the var1 is non-zero and non-null but var2 is zero.
