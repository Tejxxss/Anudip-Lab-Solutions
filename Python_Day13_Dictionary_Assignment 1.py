# Question: Write a Python program and calculate the mean of the below dictionary.
# test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

# Given dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the sum of the dictionary values
total_sum = sum(test_dict.values())  # Sum of all values in the dictionary

# Calculate the number of items (keys) in the dictionary
num_items = len(test_dict)  # Count of keys in the dictionary

# Calculate the mean
mean = total_sum / num_items  # Formula for mean = sum of values / number of items

# Output the result
print(f"Mean of the dictionary is: {mean}")

# Output: 6.2
