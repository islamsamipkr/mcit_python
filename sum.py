def sum_of_two_numbers(num1, num2):
    """Computes the sum of two numbers.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        
    Returns:
        float: The sum of the two numbers.
    """
    return num1 + num2

# Request user input for num1 and num2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function with user-provided input
result = sum_of_two_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)
