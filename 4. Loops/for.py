
# for loop

# syntax:

# for iterating_var in sequence:
#     statement(s)

# examples:

for letter in "Python":
    print("Current letter : ", letter)
    
fruits = ["apple", "mango", "banana"]
for fruit in fruits:
    print ("Current fruit : ", fruit)
    
print("Good Bye!")

# iterating by sequence index

fruits = ["apple", "mango", "banana"]
for index in range(len(fruits)):
    print ("Current fruit : ", fruits[index])
    
print("Good Bye!")

# here we took assistance of len() built-in function.

# Using else statement with loop

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print ("{0} equals {1}*{2}".format(num,i,int(j)))
            break
    else:
        print(num, "is the prime number.")
        
# the above exmple is for finding the prime number.        
            
