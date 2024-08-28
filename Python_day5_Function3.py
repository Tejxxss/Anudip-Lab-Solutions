# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
import random

# Generate a list of 5 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated random numbers
print("Numbers:", numbers)

# Display the maximum and minimum values from the list of numbers
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Expected Output (example):
# If the random numbers are [23, 67, 89, 12, 45], the output will be:
# Numbers: [23, 67, 89, 12, 45]
# Maximum: 89
# Minimum: 12