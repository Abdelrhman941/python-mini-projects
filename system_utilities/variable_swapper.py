# Input two variables
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
# Display the original values
print(f"Original values: a = {a}, b = {b}")
# Swap the values using a temporary variable
temp = a
a = b
b = temp
# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")
###############################################################
# a = 5
# b = 10
# # Swapping without a temporary variable
# a, b = b, a
# print("After swapping:")
# print("a =", a)
# print("b =", b)