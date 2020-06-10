# identity operator compares the memory location of two variables

# let

a = 20
b = 20

# is operator
print(a is b)  # if both have the same memory address will print true

print(id(a) == id(b))  # same work as above

# is not operator
print(a is not b)  # print true when a and b don't have same memory address