# this is the list of operator precedence
# like in a statement with more than one operator 
# which to solve first is according to this order

#   operator                description

#   **                      exponential 

#   ~  +  -                   complement, unary plus and minus

#   *  /  %  //                multiply, divide, modulo, and floor division

#   +  -                     addition and substraction

#   >>  <<                   right and left bitwise shift

#   &                       bitwise 'AND'

#   ^  |                     bitwise exclusive 'OR' and regular 'OR'

#   <=  <  >  >=               comparision operator

#   <>  ==  !=                equality operator

#   =  %=  /=  //=             assignment operator

#   -=  +=  *=  **=            assignment operator

# is  is not                 identity operator

# in  not in                 membership operator

# not  or  and                logical operator


# now lets look at some examples

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # (30*15) / 5
print(e)

e = ((a + b) * c) / d  # (30*15) / 5
print(e)

e = (a + b) * (c / d)  # (30)*(15/5)
print(e)

e = a + (b * c) / d  # 20 + (150/5)
print(e)

# you will observe that all the above values of e are same