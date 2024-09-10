# Question 2: Write a Python program to get the largest and smallest number from a list without builtin functions.

# Function to find the largest and smallest number in a list
def find_largest_smallest(lst):
    # Assume the first item is both the largest and smallest initially
    smallest = lst[0]
    largest = lst[0]
    
    # Loop through the list to find the actual largest and smallest
    for num in lst:
        # If current number is smaller than 'smallest', update 'smallest'
        if num < smallest:
            smallest = num
        # If current number is larger than 'largest', update 'largest'
        if num > largest:
            largest = num
    
    # Return both largest and smallest numbers
    return largest, smallest

# Example list to test the function
numbers = [2, 8, 4, 6, 10, 3]
# Calling the function and storing the result
largest, smallest = find_largest_smallest(numbers)
# Printing the results
print("Largest number:", largest)
print("Smallest number:", smallest)

# Output:
# Largest number: 10
# Smallest number: 2
