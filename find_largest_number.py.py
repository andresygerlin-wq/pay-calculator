# Program to find the largest number in a list
# Initialize variable with a very small value
largest_so_far = -1
print("before",largest_so_far)

# Iterate through each number in the list
for the_num in [9, 41, 12, 3, 74, 15]:
    # Compare current number with the largest found so far
    if the_num > largest_so_far:
        # If we found a larger one, update our record
        largest_so_far = the_num
        # Show progress in each iteration  
    print(largest_so_far, the_num)

# Display final result
print("after",largest_so_far)
