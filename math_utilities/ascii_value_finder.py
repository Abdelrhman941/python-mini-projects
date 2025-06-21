name = input("Enter name or character: ")
ascii_list = [ord(char) for char in name]
print(f"Your ASCII values: {ascii_list}")
