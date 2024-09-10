# Question 3: Write a Python program to find duplicate values from a list and display those.

# Function to find duplicate values in a list
def find_duplicates(lst):
    # List to store the duplicate values
    duplicates = []
    # Set to keep track of items we've already seen
    seen = set()
    
    # Loop through the list
    for num in lst:
        # If the number is already in 'seen' and not in 'duplicates', add it to duplicates
        if num in seen and num not in duplicates:
            duplicates.append(num)
        # Add the current number to the 'seen' set
        seen.add(num)
    
    # Return the list of duplicate numbers
    return duplicates

# Example list to test the function
numbers = [2, 4, 6, 8, 4, 6, 10, 12]
# Calling the function and printing the result
print("Duplicate values:", find_duplicates(numbers))

# Output:
# Duplicate values: [4, 6]
