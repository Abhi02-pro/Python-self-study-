
name = ['Jeff', 'Gary', 'Jill', 'Samantha']

# one form of concatenation
for n in name:
    print('Hello ! This is ' + n + '.')
    

# other form of concatenation
for n in name:
    print(" ".join(["Hey ! This is",n]))

# printing list element as comma separated strings
print(", ".join(name))


# Another fairly common string joining task is with file paths.
# It can be very tempting to do something like:

# /starting/file/path + '/' + filename

# As you may have guessed, this is not the correct method.
# Instead, we use os.path.join. For example:

# double back-slash for window's nonsense.

# location_of_files = 'C:\\Users\\H\\Desktop\\Intermediate Python'
# file_name = 'example.txt'

# with open(os.path.join(location_of_files, file_name)) as f:
#     print(f.read())

# Next, let's talk about string formatting.
# Let's consider that you want to insert variables into a string, like:
# ____ bought ____ apples today!
# ...where we want to fill in the blanks, with python variables:

who = "Ram"
how_many = 10

print("{} bought {} apples.".format(who, how_many))

# this was some playing with strings