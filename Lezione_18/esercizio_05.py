'''
An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases 
using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists of a number,
 an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), 
 and check whether the resulting list is valid:
     If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
    Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). 
    Catch any ValueError that occurs, and instead raise a FormulaError.
    If the second input is not '+' or '-', again raise a FormulaError.
    If the input is valid, perform the calculation and print out the result. 
    The user is then prompted to provide new input, and so on, until the user enters quit.
'''

class Calculator:

    def __init__(self, x:float, y: float):
        self.x = x
        self.y = y
    
    

    
