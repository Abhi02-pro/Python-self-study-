# In this part, we're going to talk about the built-in function: enumerate.

# Take this example 

example = ["left", "right", "up", "down"]

for i in range(len(example)):
    print(i, example[i])

# This can be done in another way using enumerate

for i, j in enumerate(example):
    print(i, j)


# getting on to the one liner

[print(i, j) for i, j in enumerate(example)]


#  all the above three codes produce the same output