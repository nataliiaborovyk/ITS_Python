'''
Write a function sumInRange that calculates the sum of all integers between a and b, inclusive, where a and b are passed as
input to the function.
To solve the exercise, it is mandatory to use a while loop, and it is assumed that the value of b is always greater than the
value of a. Therefore, if a > b, it is necessary to swap the values to ensure that a is the smaller of the two.
Finally, it is allowed to declare only one variable, in addition to the function parameters, to store the sum.
Then, call the function sumInRange for a = 5, b = 10 and for a = 10, b = 5
'''
def recursiveSuminrange(a,b):
    if a > b:
        temp = a
        a = b
        b = temp

    if  b == a:
        return int(a)
    
    else:
        return b + recursiveSuminrange(a, b-1)
    
print(recursiveSuminrange(2,6))

print(recursiveSuminrange(6,2))


