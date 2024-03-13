def sum(num1,num2,num3):
    return num1+num2+num3

while True:
    try:
        # Prompt for the first number
        first_number = int(input("Enter the first number: "))

        # Prompt for the second number
        second_number = int(input("Enter the second number: "))

        # Prompt for the third number
        third_number = int(input("Enter the third number: "))

        # Calculate and print the sum
        print("The sum of three numbers is:", sum(first_number, second_number, third_number))

        # Prompt whether to continue
        while True:
            choice = input("Do you want to continue? (yes/no): ").lower()
            if choice in ['yes', 'no']:
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

        if choice == 'no':
            print("Exiting the program.")
            break
    except ValueError:
        print("Invalid input! Please enter an integer.")