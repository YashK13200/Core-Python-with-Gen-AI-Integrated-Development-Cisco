""" Python program to demonstrate exception handling."""  # Module docstring

# Define a value that cannot be converted to an integer.
text_value = "abc"  # Invalid numeric text.

try:  # Start the code that may raise an exception.
	print("Attempting to convert text to an integer...")  # Show what the program is doing.
	number = int(text_value)  # This will raise a ValueError.
	print("Converted number:", number)  # This runs only if conversion succeeds.
except ValueError:  # Catch the conversion error.
	print("Exception handled: the value cannot be converted to an integer.")  # Handle the error.
else:  # This block runs only if no exception occurs.
	print("No exception occurred.")  # Confirm success.
finally:  # This block always runs.
	print("Program execution completed.")  # End message.
