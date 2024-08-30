# 1.Python program to check if the given string is a palindrome 
def is_palindrome(s):
    # Step 1: Convert the string to lowercase to ensure case-insensitivity
    s = s.lower()
    
    # Step 2: Reverse the string using slicing
    reversed_s = s[::-1]
    
    # Step 3: Compare the original string with the reversed string
    if s == reversed_s:
        return True
    else:
        return False

# Input string
input_string = "Madam"

# Step 4: Check if the input string is a palindrome
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')




# Input: "Madam"
# Output: "Madam" is a palindrome.

# Input: "Hello"
# Output: "Hello" is not a palindrome.
