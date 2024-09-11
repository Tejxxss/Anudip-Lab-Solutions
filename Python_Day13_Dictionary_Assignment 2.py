# Question: Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary: dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50, 6:60}

# Given dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the dictionaries using dictionary unpacking (**)
merged_dict = {**dic1, **dic2, **dic3}

# Output the result
print(f"Concatenated dictionary is: {merged_dict}")

# Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
