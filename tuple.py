# Create a tuple
foods = ("nasi lemak", "roti canai", "waffle", "nasi ayam")

example_tuple = ("a", 1, 2.3, "b")

# Access elements by index
first_food = foods[0]
last_food = foods[-1]

# Iterate through the tuple
print("Foods:")
for food in foods:
    print(food)

# Check if an element is in the tuple
contains_waffle = "waffle" in foods

# Find the length of the tuple
num_foods = len(foods)

# Concatenate two tuples
more_foods = ("mee siam", "ayam goreng")
all_foods = foods + more_foods

# Nested tuple
nested_tuple = ("purple", ("brown", "black"))

# Print the results
print("First food:", first_food)
print("Last food:", last_food)
print("Does it contain 'waffle'? ", contains_waffle)
print("Number of foods:", num_foods)
print("All foods:", all_foods)
print("Nested tuple:", nested_tuple)

