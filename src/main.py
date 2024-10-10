'''
Combining operations
'''
from operations import summation, subtraction

def perform_operation(num1, num2, operation):
    if operation == "add":
        result = summation(num1, num2)
    elif operation == "subtract":
        result = subtraction(num1, num2)
    else:
        raise ValueError("Invalid operation. Please choose 'add' or 'subtract'.")

    return result

from operations import division, multiplication

def divormultiply(num1, num2, operation):
	if operation =='divide':
		result = division(num1, num2)
	elif operation == 'multiplication':
		result = multiplication(num1, num2)
	else:
	     raise ValueError("invalid operation, choose 'divide' or 'multiplication"

