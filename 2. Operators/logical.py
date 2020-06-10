# defining two variables

a = 5
b = 2

print(a == 5 and b == 2)  # and gives true when both conditions are true
print(a > 5 and b == 2)

print(a > 2 or b < 2)  # or gives true if any one of the condition is true
print(a == 2 or b > 5)

 # not gives opposite of whatever is the condition returns
print(not (a == b))   # gives true if condition returns false
print(not (a > b))   # gives false if condition returns true