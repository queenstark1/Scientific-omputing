import numpy as np

# Sensor readings in degrees Celsius
temperatures = np.array([20, 22, 24, 26, 38])

# Calculate the average temperature
average = np.mean(temperatures)

# Find the lowest and highest readings
lowest = np.min(temperatures)
highest = np.max(temperatures)

print("Temperature readings:", temperatures)
print("Average temperature:", average)
print("Lowest temperature:", lowest)
print("Highest temperature:", highest)