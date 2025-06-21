def filter_list(lst):
    # Initialize an empty list to store non-string elements
    result = []
    # Iterate through the elements in the input list
    for element in lst:
        # Check if the element is a non-negative integer (not a string)
        if isinstance(element, int) and element >= 0:
            result.append(element)
    
    print(result)


filter_list([1, 2, "asf", "1", "123", 123])
