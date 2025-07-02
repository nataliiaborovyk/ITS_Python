'''
Exercise 2: Print the Sum of a Current Number and a Previous number
Write a Python code to iterate the first 10 numbers, and in each iteration, 
print the sum of the current and previous number.
'''

print("Print current anc previos number sum in range(10)")
for i in range(11):
    current_num = i
    if i == 0:
        previous_num = 0
    else:
        previous_num = i - 1
    somma = current_num + previous_num
    print(f"Current Number: {current_num}, Previous Number: {previous_num}, Somma: {somma}")