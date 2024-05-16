# Create a list of numbers
numbers = [1,4,5,7,9,10]

# Print the list
print("Original list:", numbers)

# Access elements by index
first_element = numbers[0]
print("The first element is:", first_element)


# Slice the list to get a subset
subset = numbers[1:3]
print("Subset of the list:", subset)

# Modify an element in the list
numbers[2] = 17
print("Modified list:", numbers)



# Append an element to the end of the list
numbers.append(20)
print("List after appending 20:", numbers)

# Remove an element by value
numbers.remove(4)
print("List after removing 4:", numbers)


# Find the index of an element
index_of_17 = numbers.index(17)
print("Index of 17:", index_of_17)

# Check if an element is in the list
contains_18 = 18 in numbers
print("Does the list contain 18?", contains_18)


# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

 
# Create a list of strings
drinks = ["teh o ais", "teh o limau ais", "limau ais", "jus oren"]

print(drinks[2])
