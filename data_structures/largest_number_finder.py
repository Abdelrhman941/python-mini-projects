numbers = [30, 10, -45, 5, 20]
# Initialize a variable to store the maxmium value, initially set to th
maxmium = numbers[0]
# Iterate through the list and update the maxmium value if a smaller nu
for i in numbers:
    if i > maxmium:
        maxmium = i
# Print the maxmium value
print("The largest number in the list is:", maxmium)