def basic_math_operations(num1, num2):
    # Addition
    addition = num1 + num2
    print("Addition:", addition)

    # Subtraction
    subtraction = num1 - num2
    print("Subtraction:", subtraction)

    # Multiplication
    multiplication = num1 * num2
    print("Multiplication:", multiplication)

    # Division
    # Check if num2 is not zero to avoid division by zero error
    if num2 != 0:
        division = num1 / num2
        print("Division:", division)
    else:
        print("Division by zero is not allowed.")

    # Exponentiation (num1 raised to the power of num2)
    exponentiation = num1 ** num2
    print("Exponentiation:", exponentiation)

    # Integer division (floor division)
    integer_division = num1 // num2
    print("Integer Division:", integer_division)

    # Modulo (remainder of division)
    modulo = num1 % num2
    print("Modulo:", modulo)

if __name__ == "__main__":
    # Example numbers
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the second Number: "))
    
    # Call the function with the example numbers
    basic_math_operations(num1, num2)
