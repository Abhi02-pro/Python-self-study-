
#  In this part, we're going to talk about the timeit module.

# The idea of the timeit module is to be able to test snippets of code.

# The actual code for a generator:

# input_list = range(100)

# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False

# generator, converted to list.
# xyz = list(i for i in input_list if div_by_five(i))

# The code for list comprehension:

# input_list = range(100)

# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False

# generator:
# xyz = [i for i in input_list if div_by_five(i)]

import timeit

print(timeit.timeit('1+3', number=5000000))

# This tells us how long it took to run 500,000 iterations of 1+3.

# We can also use the timeit module against multiple lines of code:

# Our generator

print(timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = (i for i in input_list if div_by_two(i))
''', number=50000))

# List comprehension:

print(timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = [i for i in input_list if div_by_two(i)]
''', number=50000))