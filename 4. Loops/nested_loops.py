
# python programming allows you to use one loop inside another loop.

# syntax for nested for loop:
# for iterating_variable in sequence:
#     for iterating_variable in sequence:
#         statemrnt(s)
#     statement(s)

# syntax for nested while loop:
# while expression:
#     while expression:
#         statement(s)
#     statement(s)

# Note : you can put any type of loop inside any type of loop.

# example:
# program to find the prime numbers from 2 to 100.

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j += 1
    if (j > i / j): print(i, "is prime.")
    i += 1

print("Good Bye")

# run the above code and check the answer.