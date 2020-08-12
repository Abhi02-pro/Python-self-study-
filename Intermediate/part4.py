
# List comprehension and generator expressions

# If you want iterate through something 4 times, you might say something like:
for i in range(4):
    """do_something"""

# What's range() doing here? In this case, it's a generator,
# so it's generating the values in order on-the-fly. 

# An example of a generator expression:
xyz = (i for i in range(10))
print(list(xyz))

# An example of list comprehension:

xyz = [i for i in range(10)]
print(xyz)

# These look and appear to act very similarly, 
# but they are quite different under the hood. 
# First, with a generator, the values are generated from an original input, 
# but the values are not copied and instead are generated on-the-fly. 
# This means we will use far less memory, 
# since the entire list is not processed all at once, 
# but also means the process is a bit slower, 
# since things are indeed generated as we go.

# The list comprehension puts the entire list into memory, 
# so it is faster, but the penalty is memory use.