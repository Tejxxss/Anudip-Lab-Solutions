import matplotlib.pyplot as plt

# 2. Visualize the daily temperature changes over time in a city.
#    - What is the temperature for each day of the month?
#    - How does the temperature fluctuate over the days?
#    - What conclusions can be drawn from the temperature trends?

# Input data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create a line chart
plt.figure(figsize=(12, 6))
plt.plot(days, temperature, marker='o', color='orange')
plt.title('Daily Temperature Changes Over a Month')
plt.xlabel('Days')
plt.ylabel('Temperature in Fahrenheit')
plt.xticks(days)  # Show every day on the x-axis
plt.grid()

# Show the plot
plt.show()

# Conclusion
average_temp = sum(temperature) / len(temperature)
max_temp = max(temperature)
min_temp = min(temperature)
print(f'Average Temperature: {average_temp:.2f}°F')
print(f'Maximum Temperature: {max_temp}°F')
print(f'Minimum Temperature: {min_temp}°F')
