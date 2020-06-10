# bitwise operators perform operations bit by bit

# assign variables

a = 0o111100  # a = 60

b = 0o1101  # b = 13

# Binary And operator
print(a & b)  # a & b = 12

# Binary Or operator
print(a | b)  # a | b = 62

# Binary XOR operator
print(a ^ b)  # a ^ b = 49

# Ones Complement operator ( unary operator - has the effect of flipping bits)
print(~a)  # ~ a = -61

# Binary Left Shift operator
print(a << 2)  # a << 2 = 240

# Binary Right Shift operator
print(a >> 2)  # a >> 2 = 15

# when you run the above codes
# the results are in octal form not in decimal form
# the decimal form is commentd in the code