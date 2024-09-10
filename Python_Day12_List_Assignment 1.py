# Question 1: Write a Python program to sum all the items in a list.

# Function to calculate the sum of all items in a list
def sum_of_list(lst):
    # Initialize a variable to store the sum
    total = 0
    # Loop through each item in the list
    for item in lst:
        # Add the item to the total sum
        total += item
    # Return the total sum
    return total

# Example list to test the function
numbers = [1, 2, 3, 4, 5]
# Calling the function and printing the result
print("Sum of the list:", sum_of_list(numbers))

# Output:
# Sum of the list: 15
