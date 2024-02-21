def string_manipulation(text):
    # Print the original text
    print("Original text:", text)

    # Convert the text to uppercase
    uppercase_text = text.upper()
    print("Uppercase:", uppercase_text)

    # Convert the text to lowercase
    lowercase_text = text.lower()
    print("Lowercase:", lowercase_text)

    # Capitalize the first letter of each word
    capitalized_text = text.title()
    print("Capitalized:", capitalized_text)

    # Replace a substring
    replaced_text = text.replace("world", "Python")
    print("Replaced:", replaced_text)

    # Check if the text starts with a specific prefix
    starts_with_hello = text.startswith("Hello")
    print("Starts with 'Hello':", starts_with_hello)

    # Check if the text ends with a specific suffix
    ends_with_world = text.endswith("world")
    print("Ends with 'world':", ends_with_world)

if __name__ == "__main__":
    # Example text
    text = "Hello, world! Welcome to Python string manipulation."
    input_from_user=input("Provide a string to see the outcome:")
    # Call the function with the example text
    string_manipulation(input_from_user)
