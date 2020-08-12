
# More on list comprehension and generators

# Let's show a more realistic use case for generators and list comprehension:

# Generator expression with a function:

input_list = [5, 65, 20, 1, 6, 35, 10, 12]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# Generator expression with a function: 

xyz = (i for i in input_list if div_by_five(i))
print(list(xyz))

# What we're doing is going through input_list, 
# and seeing if the number is divisble by five. 
# If it is, then we're putting it in a new list. 
# With the generator, we didn't copy input_list, 
# we went through it one step at a time, 
# and then only populated the new list if the number was indeed divisible by five.

# Let's do this with list comprehension:

xyz = [i for i in input_list if div_by_five(i)]
print(xyz)


# You don't have to have an if statement or 
# a function to be at the end, you could do:

[print(i) for i in range(5)]

# You could have any function in place of the print(i).

# You can also embed:

[[print(i,j) for j in range(3)] for i in range(5)]



