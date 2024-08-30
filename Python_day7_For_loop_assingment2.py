# 2.Python program to check if a given number is an Armstrong number
def is_armstrong_number(n):
    # Convert the number to a string to easily iterate through digits
    digits = str(n)
    
    # Calculate the number of digits
    num_digits = len(digits)
    
    # Initialize sum to 0 for accumulating the sum of powers of digits
    sum_of_powers = 0
    
    # Iterate through each digit in the number
    for digit in digits:
        # Convert the digit back to an integer and raise it to the power of num_digits
        sum_of_powers += int(digit) ** num_digits
    
    # Compare the sum of powers with the original number
    if sum_of_powers == n:
        # If they are equal, the number is an Armstrong number
        return True
    else:
        # If they are not equal, the number is not an Armstrong number
        return False

# Input number
input_number = 153

# Check if the input number is an Armstrong number
if is_armstrong_number(input_number):
    print(f'{input_number} is an Armstrong number.')  # Output: 153 is an Armstrong number.
else:
    print(f'{input_number} is not an Armstrong number.')  # Output: 153 is not an Armstrong number.



# Input: 153
# Output: 153 is an Armstrong number.

# Input: 123
# Output: 123 is not an Armstrong number.
