# Program to find the smallest number in a list
# Initialize variable with a big value
smallest = None
print("before",smallest)

# Iterate through each number in the list
for value in [9, 41, 12, 3, 74, 15]:
    # Check if this is the first number we're processing
    if smallest is None:
        # If it's the first number, it becomes our initial smallest
        smallest = value
    # Otherwise, compare with current smallest
    elif value < smallest:
        # If we found a smaller one, update our record
        smallest = value
    # Show progress in each iteration
    print(smallest,value)

# Display final result
print("after",smallest)
